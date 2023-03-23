import streamlit as st


class Select_Yolo:
    def select_yolo(self):
        self.zhanshi = st.sidebar.subheader("样例效果展示")
        self.img_show = st.sidebar.image("/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/images/zidane.jpg",
                                         caption="原始图片")
        self.img_show = st.sidebar.image(
            "/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/image_show/zidane_res.jpg", caption="效果图片")
