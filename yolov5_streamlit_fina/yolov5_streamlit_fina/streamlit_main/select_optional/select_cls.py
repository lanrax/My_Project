import streamlit as st


class select_class():
    def FALGS(self):
        verbose_index = (False, True)
        async_index = (False, True)
        streaming_index = (False, True)
        model_name_index = ("inception_graphdef", "yolov5_onnx", "densenet_onnx")
        model_version_index = ("", "1")
        scaling_index = ("INCEPTION",)
        # url_index = ("192.168.1.109:8004", "192.168.1.109:8005", "192.168.1.109:8006")
        url_index = ("1.117.71.120:6000", "192.168.1.109:8004", "192.168.1.109:8006")
        protocol_index = ("HTTP", "grpc")
        path_index = ("data/images/car.jpg", "data/images/bus.jpg")
        self.verbose = st.sidebar.selectbox("verbose", verbose_index)
        self.async_set = st.sidebar.selectbox("选择async", async_index)
        self.streaming = st.sidebar.selectbox("选择streaming", streaming_index)
        self.model_name = st.sidebar.selectbox("选择model_name", model_name_index)
        self.model_version = st.sidebar.selectbox("选择model_version", model_version_index)
        self.scaling = st.sidebar.selectbox("选择scaling", scaling_index)
        self.url = st.sidebar.selectbox("选择url", url_index)
        self.protocol = st.sidebar.selectbox("选择protocol", protocol_index)
        self.batch_size = st.sidebar.slider("选择Batch Size", min_value=1, max_value=24, value=None, step=None,
                                            format=None)
        self.classes = st.sidebar.slider("选择类别数量", min_value=1, max_value=100, value=None, step=None, format=None)
        self.image_filename = st.sidebar.selectbox("选择图片路径", path_index)
        self.dic = {"verbose": self.verbose, "async_set": self.async_set, "streaming": self.streaming,
                    "model_name": self.model_name , "model_version": self.model_version, "scaling": self.scaling,
                    "url": self.url, "protocol": self.protocol,
                    "batch_size": self.batch_size, "classes": self.classes, "image_filename": self.image_filename}

