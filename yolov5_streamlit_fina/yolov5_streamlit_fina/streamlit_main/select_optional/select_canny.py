import streamlit as st


class Select_Canny:
    def Parmas(self):
        path_index = ("/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/images/zishi.png",)
        self.path = st.sidebar.selectbox("选择图片路径", path_index)
        self.threshold1 = st.sidebar.slider("阈值1", min_value=0, max_value=150, value=None, step=None, format=None)
        self.threshold2 = st.sidebar.slider("阈值2", min_value=0, max_value=300, value=None, step=None, format=None)
