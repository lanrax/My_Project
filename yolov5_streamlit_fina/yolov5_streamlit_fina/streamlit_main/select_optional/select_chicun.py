import streamlit as st


class Select_chicun:
    def Parmas(self):
        # path_index = ("/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/images/zishi.png",)
        # self.path = st.sidebar.selectbox("选择图片路径", path_index)
        self.zhanshi = st.sidebar.subheader("样例效果展示")
        self.img_show = st.sidebar.image(
            "/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/images/tupian.jpg",
            caption="原始图片")
        self.img_show = st.sidebar.image(
            "/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/image_show/tupian_res.jpg", caption="效果图片")
