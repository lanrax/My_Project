import streamlit as st


class Select_3D:
    def select_3d(self):
        model_index = ('Shoe', 'Chair', 'Cup', 'Camera')
        self.model_name = st.sidebar.selectbox("选择检测物品种类", model_index)
        self.zhanshi = st.sidebar.subheader("样例效果展示")
        self.img_show = st.sidebar.image(
            "/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/images/chair.jpg",
            caption="原始图片")
        self.img_show = st.sidebar.image(
            "/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/image_show/chair_res.png", caption="效果图片")