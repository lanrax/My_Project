import streamlit as st


class Face_detection:
    def face_detection(self):
        self.zhanshi = st.sidebar.subheader("样例效果展示")
        self.img_show = st.sidebar.image("/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/images/renlian.jpg",
                                         caption="原始图片")
        self.img_show = st.sidebar.image(
            "/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/image_show/renlian_res.png", caption="效果图片")
