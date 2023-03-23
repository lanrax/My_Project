import streamlit as st


class select_param:

    # parser.add_argument('--nosave', action='store_true',
    #                     help='do not save images/videos')

    # parser.add_argument('--update', action='store_true',
    #                     help='update all models')
    def sel(self):
        weights_index = ("weights/yolov5s.pt", "weights/yolov5x.pt",)
        source_index = ("data/images/car.jpg", "data/images/bus.jpg")
        device_index = ("", "0", "1")
        img_size_index = [600, 400]
        view_img_index = ("True", "False")
        save_txt_index = ("True", "False")
        project_index = ("runs/detect",)
        name_index = ("exp", "exp1")
        nosave_index = ("False", "True")
        augment_index = ("True", "False")
        conf_thres_index = [0.35, 0.40, 0.5]
        iou_thres_index = [0.3, 0.45, 0.5]
        save_conf_index = ("True", "False")
        classes_index = [0, 1, 2, 3]
        agnostic_nms_index = ("True", "False")
        update_index = ("True", "False")
        self.weights = st.sidebar.selectbox("选择模型权重", weights_index)
        self.source = st.sidebar.selectbox("选择图片", source_index)
        self.device = st.sidebar.selectbox("选择设备", device_index)
        self.img_size = st.sidebar.selectbox("选择图片大小", img_size_index)
        self.view_img = st.sidebar.selectbox("选择可视化", view_img_index)
        self.save_txt = st.sidebar.selectbox("选择save_txt", save_txt_index)
        self.project = st.sidebar.selectbox("选择项目地址", project_index)
        self.name = st.sidebar.selectbox("选择name_index", name_index)
        self.nosave = st.sidebar.selectbox("选择是否保存", nosave_index)
        self.augment = st.sidebar.selectbox("选择augment", augment_index)
        self.conf_thres = st.sidebar.selectbox("选择置信度", conf_thres_index)
        self.iou_thres = st.sidebar.selectbox("选择交并比", iou_thres_index)
        self.save_conf = st.sidebar.selectbox("save_conf", save_conf_index)
        self.classes = st.sidebar.selectbox("选择类别个数", classes_index)
        self.agnostic_nms = st.sidebar.selectbox("选择是否极大抑制", agnostic_nms_index)
        self.update = st.sidebar.selectbox("选择是否更新", update_index)
