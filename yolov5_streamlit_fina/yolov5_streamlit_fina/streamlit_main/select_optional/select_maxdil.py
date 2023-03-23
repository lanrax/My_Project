import streamlit as st


class Select_Dil:
    def select_dil(self):
        # path_index = ("/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/images/bus.jpg",)
        # self.path = st.sidebar.selectbox("选择图片路径", path_index)
        self.threshold1 = st.sidebar.slider("阈值1", min_value=0, max_value=150, value=50, step=None, format=None)
        self.threshold2 = st.sidebar.slider("阈值2", min_value=0, max_value=300, value=100, step=None, format=None)
        self.zhanshi = st.sidebar.subheader("样例效果展示")
        self.img_show = st.sidebar.image(
            "/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/images/tupian.jpg",
            caption="原始图片")
        self.img_show = st.sidebar.image(
            "/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/image_show/max_dil.jpg", caption="效果图片")
