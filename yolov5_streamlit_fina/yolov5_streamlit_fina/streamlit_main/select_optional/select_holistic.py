import streamlit as st


class Select_Hos:
    def holistic(self):
        # path_index = ("/home/hadoop/yolov5_streamlit_test/data/images/zishi.png",)
        # self.path = st.sidebar.selectbox("选择图片路径", path_index)
        self.zhanshi = st.sidebar.subheader("样例效果展示")
        self.img_show = st.sidebar.image("/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/images/Hos.jpg",
                                         caption="原始图片")
        self.img_show = st.sidebar.image(
            "/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/image_show/Hos_res.png", caption="效果图片")
