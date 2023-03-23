import cv2
import torch
from PIL import Image
from eyedetected.yolov5 import detect
# from my_client.myclient import my_infer
from pathlib import Path
import os
import sys
import shutil
from filepath.settings import example_img, yolo_img, image_save
from eyedetected.classi import run_cls
from eyedetected.opencv_preocess import ill_yolo
import time

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
model_weight = "/home/hadoop/eme/eyedetected/eyedetected/eye/weights/"


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def elite_infer(engine="Pytorch", file_path=example_img):
    """
    :param engine: 框架类型
    :param url:
    :return:
    """
    engine_model = {
        "Pytorch": ".pt",
        "ONNX": ".onnx",
        "TorchScript": ".torchscript",
        "RKNN": ".rknn",
        "TensorRT": ".engine"
    }
    del_file(str(yolo_img) + '/detect')
    res = detect.run(weights=model_weight + 'yolov5s' + engine_model[engine],
                     # model path or triton URL
                     # source=ROOT / 'data/images/bus.jpg',  # file/dir/URL/glob/screen/0(webcam)
                     source=file_path,  # file/dir/URL/glob/screen/0(webcam)
                     data=ROOT / 'data/coco128.yaml',  # dataset.yaml path
                     imgsz=(640, 640),  # inference size (height, width)
                     conf_thres=0.25,  # confidence threshold
                     iou_thres=0.45,  # NMS IOU threshold
                     max_det=1000,  # maximum detections per image
                     device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
                     )

    return res


def fire_infer(engine="TensorRT", file_path=example_img):
    """
    :param engine: 框架类型
    :param url:
    :return:
    """
    engine_model = {
        "Pytorch": ".pt",
        "ONNX": ".onnx",
        "TorchScript": ".torchscript",
        "RKNN": ".rknn",
        "TensorRT": ".engine"
    }
    del_file(str(yolo_img) + '/detect')
    res = detect.run(weights=model_weight + 'fire' + engine_model[engine],
                     # model path or triton URL
                     # source=ROOT / 'data/images/bus.jpg',  # file/dir/URL/glob/screen/0(webcam)
                     source=file_path,  # file/dir/URL/glob/screen/0(webcam)
                     data=ROOT / 'data/coco128.yaml',  # dataset.yaml path
                     imgsz=(640, 640),  # inference size (height, width)
                     conf_thres=0.25,  # confidence threshold
                     iou_thres=0.45,  # NMS IOU threshold
                     max_det=1000,  # maximum detections per image
                     device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
                     )

    return res
