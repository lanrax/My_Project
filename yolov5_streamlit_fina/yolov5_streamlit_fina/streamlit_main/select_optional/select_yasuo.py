import streamlit as st


class select_yasuo:

    def seleyasuo(self):
        self.quality = st.sidebar.slider("选择压缩质量", min_value=0, max_value=100, value=None, step=None, format=None)
        self.zhanshi = st.sidebar.subheader("样例效果展示")
        self.img_show = st.sidebar.image("/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/image_show/bus.jpg",
                                         caption="原始图片")
        self.img_show = st.sidebar.image(
            "/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/image_show/yasuo_res.jpeg", caption="效果图片")
        # self.path = st.sidebar.selectbox("选择图片路径", path_index)
