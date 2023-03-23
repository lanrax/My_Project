import streamlit as st


class select_video:

    # parser.add_argument('--nosave', action='store_true',
    #                     help='do not save images/videos')

    # parser.add_argument('--update', action='store_true',
    #                     help='update all models')
    def sel(self):
        weights_index = ("weights/yolov5s.pt",)
        source_index = ("data/videos/10s.mp4",)
        self.weights = st.sidebar.selectbox("选择模型权重", weights_index)
        self.path = st.sidebar.selectbox("选择视频", source_index)

