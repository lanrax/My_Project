#!/usr/bin/env python
# Copyright 2020_2022, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from functools import partial
import os
import sys
from PIL import Image
import numpy as np
from attrdict import AttrDict
import tritonclient.grpc as grpcclient
import tritonclient.grpc.model_config_pb2 as mc
import tritonclient.http as httpclient
from tritonclient.utils import InferenceServerException
from tritonclient.utils import triton_to_np_dtype

if sys.version_info >= (3, 0):
    import queue
else:
    import Queue as queue


class UserData:

    def __init__(self):
        self._completed_requests = queue.Queue()


# Callback function used for async_stream_infer()
def completion_callback(user_data, result, error):
    # passing error raise and handling out
    user_data._completed_requests.put((result, error))


# FLAGS = None


def parse_model(model_metadata, model_config):
    """
    Check the configuration of a model to make sure it meets the
    requirements for an image classification network (as expected by
    this client)
    """
    if len(model_metadata.inputs) != 1:
        raise Exception("expecting 1 input, got {}".format(
            len(model_metadata.inputs)))
    if len(model_metadata.outputs) != 1:
        raise Exception("expecting 1 output, got {}".format(
            len(model_metadata.outputs)))

    if len(model_config.input) != 1:
        raise Exception(
            "expecting 1 input in model configuration, got {}".format(
                len(model_config.input)))

    input_metadata = model_metadata.inputs[0]
    input_config = model_config.input[0]
    output_metadata = model_metadata.outputs[0]

    if output_metadata.datatype != "FP32":
        raise Exception("expecting output datatype to be FP32, model '" +
                        model_metadata.name + "' output type is " +
                        output_metadata.datatype)

    # Output is expected to be a vector. But allow any number of
    # dimensions as long as all but 1 is size 1 (e.g. { 10 }, { 1, 10
    # }, { 10, 1, 1 } are all ok). Ignore the batch dimension if there
    # is one.
    output_batch_dim = (model_config.max_batch_size > 0)
    non_one_cnt = 0
    for dim in output_metadata.shape:
        if output_batch_dim:
            output_batch_dim = False
        elif dim > 1:
            non_one_cnt += 1
            if non_one_cnt > 1:
                raise Exception("expecting model output to be a vector")

    # Model input must have 3 dims, either CHW or HWC (not counting
    # the batch dimension), either CHW or HWC
    input_batch_dim = (model_config.max_batch_size > 0)
    expected_input_dims = 3 + (1 if input_batch_dim else 0)
    if len(input_metadata.shape) != expected_input_dims:
        raise Exception(
            "expecting input to have {} dimensions, model '{}' input has {}".
            format(expected_input_dims, model_metadata.name,
                   len(input_metadata.shape)))

    if type(input_config.format) == str:
        FORMAT_ENUM_TO_INT = dict(mc.ModelInput.Format.items())
        input_config.format = FORMAT_ENUM_TO_INT[input_config.format]

    if ((input_config.format != mc.ModelInput.FORMAT_NCHW) and
            (input_config.format != mc.ModelInput.FORMAT_NHWC)):
        raise Exception("unexpected input format " +
                        mc.ModelInput.Format.Name(input_config.format) +
                        ", expecting " +
                        mc.ModelInput.Format.Name(mc.ModelInput.FORMAT_NCHW) +
                        " or " +
                        mc.ModelInput.Format.Name(mc.ModelInput.FORMAT_NHWC))

    if input_config.format == mc.ModelInput.FORMAT_NHWC:
        h = input_metadata.shape[1 if input_batch_dim else 0]
        w = input_metadata.shape[2 if input_batch_dim else 1]
        c = input_metadata.shape[3 if input_batch_dim else 2]
    else:
        c = input_metadata.shape[1 if input_batch_dim else 0]
        h = input_metadata.shape[2 if input_batch_dim else 1]
        w = input_metadata.shape[3 if input_batch_dim else 2]

    return (model_config.max_batch_size, input_metadata.name,
            output_metadata.name, c, h, w, input_config.format,
            input_metadata.datatype)


def preprocess(img, format, dtype, c, h, w, scaling, protocol):
    """
    Pre_process an image to meet the size, type and format
    requirements specified by the parameters.
    """
    # np.set_printoptions(threshold='nan')

    if c == 1:
        sample_img = img.convert('L')
    else:
        sample_img = img.convert('RGB')

    resized_img = sample_img.resize((w, h), Image.BILINEAR)
    resized = np.array(resized_img)
    if resized.ndim == 2:
        resized = resized[:, :, np.newaxis]

    npdtype = triton_to_np_dtype(dtype)
    typed = resized.astype(npdtype)

    if scaling == 'INCEPTION':
        scaled = (typed / 127.5) - 1
    elif scaling == 'VGG':
        if c == 1:
            scaled = typed - np.asarray((128,), dtype=npdtype)
        else:
            scaled = typed - np.asarray((123, 117, 104), dtype=npdtype)
    else:
        scaled = typed

    # Swap to CHW if necessary
    if format == mc.ModelInput.FORMAT_NCHW:
        ordered = np.transpose(scaled, (2, 0, 1))
    else:
        ordered = scaled

    # Channels are in RGB order. Currently model configuration data
    # doesn't provide any information as to other channel orderings
    # (like BGR) so we just assume RGB.
    return ordered


def postprocess(results, output_name, batch_size, supports_batching):
    """
    Post_process results to show classifications.
    """

    output_array = results.as_numpy(output_name)

    ##

    if supports_batching and len(output_array) != batch_size:
        raise Exception("expected {} results, got {}".format(
            batch_size, len(output_array)))

    # Include special handling for non_batching models
    res = []
    for results in output_array:

        if not supports_batching:
            results = [results]
        for result in results:
            if output_array.dtype.type == np.object_:
                cls = "".join(chr(x) for x in result).split(':')
            else:
                cls = result.split(':')
            print("    {} ({}) = {}".format(cls[0], cls[1], cls[2]))
            res.append([cls[0], cls[1], cls[2]])
    return res


def requestGenerator(batched_image_data, input_name, output_name, dtype, FLAGS):
    if FLAGS.get("protocol") == "grpc":
        client = grpcclient
    else:
        client = httpclient

    # Set the input data
    inputs = [client.InferInput(input_name, batched_image_data.shape, dtype)]
    inputs[0].set_data_from_numpy(batched_image_data)

    outputs = [
        client.InferRequestedOutput(output_name, class_count=FLAGS.get("classes"))
    ]

    yield inputs, outputs, FLAGS.get("model_name"), FLAGS.get("model_version")


def convert_http_metadata_config(_metadata, _config):
    _model_metadata = AttrDict(_metadata)
    _model_config = AttrDict(_config)

    return _model_metadata, _model_config


# def my_infer(verbose, async_set, streaming, model_name, model_version, batch_size, classes, scaling, url, protocol,
#              path):
#     if streaming is True and protocol != "grpc":
#         raise Exception("Streaming is only allowed with gRPC protocol")
#
#     try:
#         if protocol == "grpc":
#             # Create gRPC client for communicating with the server
#             triton_client = grpcclient.InferenceServerClient(
#                 url=url, verbose=verbose)
#         else:
#             # Specify large enough concurrency to handle the
#             # the number of requests.
#             concurrency = 20 if async_set else 1
#             triton_client = httpclient.InferenceServerClient(
#                 url=url, verbose=verbose, concurrency=concurrency)
#     except Exception as e:
#         print("client creation failed: " + str(e))
#         sys.exit(1)
#
#     # Make sure the model matches our requirements, and get some
#     # properties of the model that we need for preprocessing
#     try:
#         model_metadata = triton_client.get_model_metadata(
#             model_name=model_name, model_version=model_version)
#     except InferenceServerException as e:
#         print("failed to retrieve the metadata: " + str(e))
#         sys.exit(1)
#
#     try:
#         model_config = triton_client.get_model_config(
#             model_name=model_name, model_version=model_version)
#     except InferenceServerException as e:
#         print("failed to retrieve the config: " + str(e))
#         sys.exit(1)
#
#     if protocol == "grpc":
#         model_config = model_config.config
#     else:
#         model_metadata, model_config = convert_http_metadata_config(
#             model_metadata, model_config)
#
#     max_batch_size, input_name, output_name, c, h, w, format, dtype = parse_model(
#         model_metadata, model_config)
#
#     supports_batching = max_batch_size > 0
#     if not supports_batching and batch_size != 1:
#         print("ERROR: This model doesn't support batching.")
#         sys.exit(1)
#
#     filenames = []
#     if os.path.isdir(path):
#         filenames = [
#             os.path.join(path, f)
#             for f in os.listdir(path)
#             if os.path.isfile(os.path.join(path, f))
#         ]
#     else:
#         filenames = [
#             path,
#         ]
#
#     filenames.sort()
#
#     # Preprocess the images into input data according to model
#     # requirements
#     image_data = []
#     for filename in filenames:
#         img = Image.open(filename)
#         image_data.append(
#             preprocess(img, format, dtype, c, h, w, scaling,
#                        protocol))
#
#     # Send requests of FLAGS.get("batch_size") images. If the number of
#     # images isn't an exact multiple of FLAGS.get("batch_size") then just
#     # start over with the first images until the batch is filled.
#     requests = []
#     responses = []
#     result_filenames = []
#     request_ids = []
#     image_idx = 0
#     last_request = False
#     user_data = UserData()
#
#     # Holds the handles to the ongoing HTTP async requests.
#     async_requests = []
#
#     sent_count = 0
#
#     if streaming:
#         triton_client.start_stream(partial(completion_callback, user_data))
#
#     while not last_request:
#         input_filenames = []
#         repeated_image_data = []
#
#         for idx in range(batch_size):
#             input_filenames.append(filenames[image_idx])
#             repeated_image_data.append(image_data[image_idx])
#             image_idx = (image_idx + 1) % len(image_data)
#             if image_idx == 0:
#                 last_request = True
#
#         if supports_batching:
#             batched_image_data = np.stack(repeated_image_data, axis=0)
#         else:
#             batched_image_data = repeated_image_data[0]
#
#         # Send request
#         try:
#             for inputs, outputs, model_name, model_version in requestGenerator(
#                     batched_image_data, input_name, output_name, dtype, protocol, classes, model_name, model_version):
#                 sent_count += 1
#                 if streaming:
#                     triton_client.async_stream_infer(
#                         model_name,
#                         inputs,
#                         request_id=str(sent_count),
#                         model_version=model_version,
#                         outputs=outputs)
#                 elif async_set:
#                     if protocol == "grpc":
#                         triton_client.async_infer(
#                             model_name,
#                             inputs,
#                             partial(completion_callback, user_data),
#                             request_id=str(sent_count),
#                             model_version=model_version,
#                             outputs=outputs)
#                     else:
#                         async_requests.append(
#                             triton_client.async_infer(
#                                 model_name,
#                                 inputs,
#                                 request_id=str(sent_count),
#                                 model_version=model_version,
#                                 outputs=outputs))
#                 else:
#                     responses.append(
#                         triton_client.infer(model_name,
#                                             inputs,
#                                             request_id=str(sent_count),
#                                             model_version=model_version,
#                                             outputs=outputs))
#
#         except InferenceServerException as e:
#             print("inference failed: " + str(e))
#             if streaming:
#                 triton_client.stop_stream()
#             sys.exit(1)
#
#     if streaming:
#         triton_client.stop_stream()
#
#     if protocol == "grpc":
#         if streaming or async_set:
#             processed_count = 0
#             while processed_count < sent_count:
#                 (results, error) = user_data._completed_requests.get()
#                 processed_count += 1
#                 if error is not None:
#                     print("inference failed: " + str(error))
#                     sys.exit(1)
#                 responses.append(results)
#     else:
#         if async_set:
#             # Collect results from the ongoing async requests
#             # for HTTP Async requests.
#             for async_request in async_requests:
#                 responses.append(async_request.get_result())
#     # myres = []
#     for response in responses:
#         if protocol == "grpc":
#             this_id = response.get_response().id
#         else:
#             this_id = response.get_response()["id"]
#         print("Request {}, batch size {}".format(this_id, batch_size))
#         postprocess(response, output_name, batch_size, supports_batching)
#
#     print("PASS")
#     # return myres

def my_infer(FLAGS):
    if FLAGS.get("streaming") is True and FLAGS.get("protocol") != "grpc":
        raise Exception("Streaming is only allowed with gRPC protocol")

    try:
        if FLAGS.get("protocol") == "grpc":
            # Create gRPC client for communicating with the server
            triton_client = grpcclient.InferenceServerClient(
                url=FLAGS.get("url"), verbose=FLAGS.get("verbose"))
        else:
            # Specify large enough concurrency to handle the
            # the number of requests.
            concurrency = 20 if FLAGS.get("async_set") else 1
            triton_client = httpclient.InferenceServerClient(
                url=FLAGS.get("url"), verbose=FLAGS.get("verbose"), concurrency=concurrency)
    except Exception as e:
        print("client creation failed: " + str(e))
        sys.exit(1)

    # Make sure the model matches our requirements, and get some
    # properties of the model that we need for preprocessing
    try:
        model_metadata = triton_client.get_model_metadata(
            model_name=FLAGS.get("model_name"), model_version=FLAGS.get("model_version"))
    except InferenceServerException as e:
        print("failed to retrieve the metadata: " + str(e))
        sys.exit(1)

    try:
        model_config = triton_client.get_model_config(
            model_name=FLAGS.get("model_name"), model_version=FLAGS.get("model_version"))
    except InferenceServerException as e:
        print("failed to retrieve the config: " + str(e))
        sys.exit(1)

    if FLAGS.get("protocol") == "grpc":
        model_config = model_config.config
    else:
        model_metadata, model_config = convert_http_metadata_config(
            model_metadata, model_config)

    max_batch_size, input_name, output_name, c, h, w, format, dtype = parse_model(
        model_metadata, model_config)

    supports_batching = max_batch_size > 0
    if not supports_batching and FLAGS.get("batch_size") != 1:
        print("ERROR: This model doesn't support batching.")
        sys.exit(1)

    filenames = []
    if os.path.isdir(FLAGS.get("image_filename")):
        filenames = [
            os.path.join(FLAGS.get("image_filename"), f)
            for f in os.listdir(FLAGS.get("image_filename"))
            if os.path.isfile(os.path.join(FLAGS.get("image_filename"), f))
        ]
    else:
        filenames = [
            FLAGS.get("image_filename"),
        ]

    filenames.sort()

    # Preprocess the images into input data according to model
    # requirements
    image_data = []
    for filename in filenames:
        img = Image.open(filename)
        image_data.append(
            preprocess(img, format, dtype, c, h, w, FLAGS.get("scaling"),
                       FLAGS.get("protocol")))

    # Send requests of FLAGS.get("batch_size") images. If the number of
    # images isn't an exact multiple of FLAGS.get("batch_size") then just
    # start over with the first images until the batch is filled.
    requests = []
    responses = []
    result_filenames = []
    request_ids = []
    image_idx = 0
    last_request = False
    user_data = UserData()

    # Holds the handles to the ongoing HTTP async requests.
    async_requests = []

    sent_count = 0

    if FLAGS.get("streaming"):
        triton_client.start_stream(partial(completion_callback, user_data))

    while not last_request:
        input_filenames = []
        repeated_image_data = []

        for idx in range(FLAGS.get("batch_size")):
            input_filenames.append(filenames[image_idx])
            repeated_image_data.append(image_data[image_idx])
            image_idx = (image_idx + 1) % len(image_data)
            if image_idx == 0:
                last_request = True

        if supports_batching:
            batched_image_data = np.stack(repeated_image_data, axis=0)
        else:
            batched_image_data = repeated_image_data[0]

        # Send request
        try:
            for inputs, outputs, model_name, model_version in requestGenerator(
                    batched_image_data, input_name, output_name, dtype, FLAGS):
                sent_count += 1
                if FLAGS.get("streaming"):
                    triton_client.async_stream_infer(
                        FLAGS.get("model_name"),
                        inputs,
                        request_id=str(sent_count),
                        model_version=FLAGS.get("model_version"),
                        outputs=outputs)
                elif FLAGS.get("async_set"):
                    if FLAGS.get("protocol") == "grpc":
                        triton_client.async_infer(
                            FLAGS.get("model_name"),
                            inputs,
                            partial(completion_callback, user_data),
                            request_id=str(sent_count),
                            model_version=FLAGS.get("model_version"),
                            outputs=outputs)
                    else:
                        async_requests.append(
                            triton_client.async_infer(
                                FLAGS.get("model_name"),
                                inputs,
                                request_id=str(sent_count),
                                model_version=FLAGS.get("model_version"),
                                outputs=outputs))
                else:
                    responses.append(
                        triton_client.infer(FLAGS.get("model_name"),
                                            inputs,
                                            request_id=str(sent_count),
                                            model_version=FLAGS.get("model_version"),
                                            outputs=outputs))

        except InferenceServerException as e:
            print("inference failed: " + str(e))
            if FLAGS.get("streaming"):
                triton_client.stop_stream()
            sys.exit(1)

    if FLAGS.get("streaming"):
        triton_client.stop_stream()

    if FLAGS.get("protocol") == "grpc":
        if FLAGS.get("streaming") or FLAGS.get("async_set"):
            processed_count = 0
            while processed_count < sent_count:
                (results, error) = user_data._completed_requests.get()
                processed_count += 1
                if error is not None:
                    print("inference failed: " + str(error))
                    sys.exit(1)
                responses.append(results)
    else:
        if FLAGS.get("async_set"):
            # Collect results from the ongoing async requests
            # for HTTP Async requests.
            for async_request in async_requests:
                responses.append(async_request.get_result())
    myres = []
    for response in responses:
        if FLAGS.get("protocol") == "grpc":
            this_id = response.get_response().id
        else:
            this_id = response.get_response()["id"]
        print("Request {}, batch size {}".format(this_id, FLAGS.get("batch_size")))
        myres = postprocess(response, output_name, FLAGS.get("batch_size"), supports_batching)

    print("PASS")
    return myres


if __name__ == '__main__':
    FLAGS = {
        "verbose": False,
        "async_set": False,
        "streaming": False,
        "model_name": 'inception_graphdef',
        "model_version": "",
        "batch_size": 1,
        "classes": 3,
        "scaling": 'INCEPTION',
        "url": '192.168.1.109:8004',
        "protocol": 'HTTP',
        "image_filename": '/home/hadoop/djangoProject1/my_client/bus.jpg'
    }
    my_infer(FLAGS)
