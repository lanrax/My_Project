import streamlit as st
# from detect import detect_1
import os
import pandas as pd
from PIL import Image
from select_optional.select_yasuo import select_yasuo
from many_func.yasuo_func import yasuo
from select_optional.select_cls import select_class
from many_func.my_test_client import my_infer
from select_optional.select_pos import Select_pos
from mediatest.postest import pos_reg
from mediatest.face_detection import face_detection
from select_optional.select_face_detection import Face_detection
from mediatest.Holistic import holistic
from select_optional.select_holistic import Select_Hos
from mediatest.detection_3D import detection_3d
from select_optional.select_3d_det import Select_3D
from select_optional.select_video import select_video
from many_func.yolov5 import detect_2
from select_optional.select_yolo import Select_Yolo
from select_optional.select_chicun import Select_chicun
from many_func.biaoding import biaoji
from many_func.Area_compute import area_compute
from select_optional.select_area import Select_Area
from many_func.neijing import max_dil
from select_optional.select_maxdil import Select_Dil


def get_subdirs(b='.'):
    '''
        Returns all sub-directories in a specific Path
    '''
    result = []
    for d in os.listdir(b):
        bd = os.path.join(b, d)
        if os.path.isdir(bd):
            result.append(bd)
    # print(result)
    return result


def get_detection_folder():
    '''
        Returns the latest folder in a runs\detect
    '''
    # print(max(get_subdirs(os.path.join('runs', 'detect')), key=os.path.getmtime))
    return max(get_subdirs(os.path.join('runs', 'detect')), key=os.path.getmtime)


if __name__ == '__main__':

    st.title('智能检测APP')

    st.sidebar.title('菁数人工智能平台')  # 在侧边加入标题
    source = (
        "图片检测", "视频检测", "图像压缩", "图像识别", "姿态估计", "人脸识别", "整体(人脸+姿态估计)", "3D检测",
        "轮廓检测", "面积计算", "最大内径")
    source_index = st.sidebar.selectbox("选择任务", range(
        len(source)), format_func=lambda x: source[x])
    is_pos = False
    is_valid = False
    is_yasuo = False
    is_cls = False
    is_face = False
    is_hos = False
    is_3D = False
    is_video = False
    is_chicun = False
    is_maxdil = False
    is_area = False

    if source_index == 0:
        opt = Select_Yolo()
        opt.select_yolo()

        uploaded_file = st.sidebar.file_uploader(
            "上传图片", type=['png', 'jpeg', 'jpg'])
        if uploaded_file is not None:
            is_valid = True
            is_yasuo = False
            is_cls = False
            is_video = False
            with st.spinner(text='资源加载中...'):
                st.sidebar.image(uploaded_file)
                picture = Image.open(uploaded_file)  # 打开选取的文件
                picture = picture.save(f'data/images/{uploaded_file.name}')  # 将打开的文件保存在该路径下
                # opt.path = f'data/images/{uploaded_file.name}'

        else:
            is_valid = False
            is_yasuo = False
            is_cls = False
    elif source_index == 1:
        opt = select_video()
        opt.sel()
        uploaded_file = st.sidebar.file_uploader("上传视频", type=['mp4'])
        if uploaded_file is not None:
            is_valid = True
            is_yasuo = False
            is_cls = False
            is_video = True
            with st.spinner(text='资源加载中...'):
                st.sidebar.video(uploaded_file)
                with open(os.path.join("data", "videos", uploaded_file.name), "wb") as f:
                    f.write(uploaded_file.getbuffer())
                # opt.path = f'data/videos/{uploaded_file.name}'

        else:
            is_valid = False
            is_yasuo = False
            is_cls = False
            is_video = False
    elif source_index == 2:
        opt = select_yasuo()
        opt.seleyasuo()
        uploaded_file = st.sidebar.file_uploader(
            "上传图片", type=['png', 'jpeg', 'jpg'])
        print("uploadfile", uploaded_file)
        if uploaded_file is not None:
            is_valid = True
            is_yasuo = True
            is_cls = False
            is_video = False
            with st.spinner(text='资源加载中...'):
                st.sidebar.image(uploaded_file)
                picture = Image.open(uploaded_file)  # 打开选取的文件
                print(f'data/images/{uploaded_file.name}')
                picture = picture.save(f'data/images/{uploaded_file.name}')  # 将打开的文件保存在该路径下
                # opt.path = f'data/images/{uploaded_file.name}'
        else:
            is_valid = False
            is_yasuo = False
            is_cls = False
            is_video = False

    elif source_index == 3:
        opt = select_class()
        opt.FALGS()

        uploaded_file = st.sidebar.file_uploader(
            "上传图片", type=['png', 'jpeg', 'jpg'])
        if uploaded_file is not None:
            is_valid = True
            is_yasuo = False
            is_cls = True
            is_video = False
            with st.spinner(text='资源加载中...'):
                st.sidebar.image(uploaded_file)
                picture = Image.open(uploaded_file)  # 打开选取的文件
                picture = picture.save(f'data/images/{uploaded_file.name}')  # 将打开的文件保存在该路径下
                opt.dic["image_filename"] = f'data/images/{uploaded_file.name}'
        else:
            is_valid = False
            is_yasuo = False
            is_cls = False
            is_video = False
    elif source_index == 4:
        opt = Select_pos()
        opt.Parmas()
        uploaded_file = st.sidebar.file_uploader(
            "上传图片", type=['png', 'jpg', 'jpeg']
        )
        if uploaded_file is not None:
            is_pos = True
            with st.spinner(text="资源加载中..."):
                st.sidebar.image(uploaded_file)
                picture = Image.open(uploaded_file)
                picture = picture.save(f'data/images/{uploaded_file.name}')
                # opt.path = f'data/images/{uploaded_file.name}'
        else:
            is_pos = False

    elif source_index == 5:
        opt = Face_detection()
        opt.face_detection()
        uploaded_file = st.sidebar.file_uploader(
            "上传图片", type=['png', 'jpg', 'jpeg']
        )
        if uploaded_file is not None:
            is_face = True
            with st.spinner(text="资源加载中..."):
                st.sidebar.image(uploaded_file)
                picture = Image.open(uploaded_file)
                picture = picture.save(f'data/images/{uploaded_file.name}')
                # opt.path = f'data/images/{uploaded_file.name}'
        else:
            is_face = False

    elif source_index == 6:
        opt = Select_Hos()
        opt.holistic()
        uploaded_file = st.sidebar.file_uploader(
            "上传图片", type=['png', 'jpg', 'jpeg']
        )
        if uploaded_file is not None:
            is_hos = True
            with st.spinner(text="资源加载中..."):
                st.sidebar.image(uploaded_file)
                picture = Image.open(uploaded_file)
                picture = picture.save(f'data/images/{uploaded_file.name}')
                # opt.path = f'data/images/{uploaded_file.name}'
        else:
            is_hos = False

    elif source_index == 7:
        opt = Select_3D()
        opt.select_3d()
        uploaded_file = st.sidebar.file_uploader(
            "上传图片", type=['png', 'jpg', 'jpeg']
        )
        if uploaded_file is not None:
            is_3D = True
            with st.spinner(text="资源加载中..."):
                st.sidebar.image(uploaded_file)
                picture = Image.open(uploaded_file)
                picture = picture.save(f'data/images/{uploaded_file.name}')
                # opt.path = f'data/images/{uploaded_file.name}'
        else:
            is_3D = False

    elif source_index == 8:
        opt = Select_chicun()
        opt.Parmas()
        uploaded_file = st.sidebar.file_uploader(
            "上传图片", type=['png', 'jpg', 'jpeg']
        )
        if uploaded_file is not None:
            is_chicun = True
            with st.spinner(text="资源加载中..."):
                st.sidebar.image(uploaded_file)
                picture = Image.open(uploaded_file)
                picture = picture.save(f'data/images/{uploaded_file.name}')
                # opt.path = f'data/images/{uploaded_file.name}'
        else:
            is_chicun = False

    elif source_index == 9:
        opt = Select_Area()
        opt.select_area()
        uploaded_file = st.sidebar.file_uploader(
            "上传图片", type=['png', 'jpg', 'jpeg']
        )
        if uploaded_file is not None:
            is_area = True
            with st.spinner(text="资源加载中..."):
                st.sidebar.image(uploaded_file)
                picture = Image.open(uploaded_file)
                picture = picture.save(f'data/images/{uploaded_file.name}')
                # opt.path = f'data/images/{uploaded_file.name}'
        else:
            is_area = False
    elif source_index == 10:
        opt = Select_Dil()
        opt.select_dil()
        uploaded_file = st.sidebar.file_uploader(
            "上传图片", type=['png', 'jpg', 'jpeg']
        )
        if uploaded_file is not None:
            is_maxdil = True
            with st.spinner(text="资源加载中..."):
                st.sidebar.image(uploaded_file)
                picture = Image.open(uploaded_file)
                picture = picture.save(f'data/images/{uploaded_file.name}')
                # opt.path = f'data/images/{uploaded_file.name}'
        else:
            is_maxdil = False

    if is_valid is True and is_yasuo is True:
        is_valid = False
        print('执行图像压缩')
        if st.button('开始压缩'):
            with st.spinner(text='Preparing Images'):
                # yasuo(opt.path, opt.quality)
                st.image(yasuo(f'data/images/{uploaded_file.name}', opt.quality))
                st.balloons()  # 页面中的气球
            # 执行opencv的图像压缩库
            print('压缩完成')

    if is_valid is True and is_yasuo is False and is_cls is False and is_video is False:
        print("执行图片目标检测")
        if st.button("开始"):
            res = detect_2(f'data/images/{uploaded_file.name}')
            ass = pd.DataFrame(res)
            st.write(ass)
            # for img in os.listdir(get_detection_folder()+'/'):
            #     st.image(get_detection_folder() + '/' + img)
            st.image('/home/hadoop/yolov5_streamlit_fina/streamlit_main/runs/detect/exp/image0.jpg')
            st.balloons()
            print("完成")
    if is_video is True:
        print("执行视频目标检测")
        if st.button("开始"):
            # main_video(opt.path)

            video_file = open('/home/hadoop/yolov5_streamlit_fina/streamlit_main/10s.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes, format="video/mp4")
            st.balloons()
            print("完成")

    if is_valid is True and is_cls is True:
        is_valid = False
        print('执行图像识别')
        if st.button('开始识别'):
            res = {"类别1": my_infer(opt.dic)[0][0],
                   # "类别2": my_infer(opt.dic)[0][1],
                   # "类别3": my_infer(opt.dic)[0][2]
                   }
            ass = pd.DataFrame(res).T
            st.write(ass)
            st.balloons()
            print('识别完成')

    if is_pos == True:
        print("执行姿态估计")
        if st.button("开始"):
            res = pos_reg(f'data/images/{uploaded_file.name}')
            st.image(res)
            st.balloons()
            print("完成")

    if is_face == True:
        print("执行人脸识别")
        if st.button("开始"):
            res = face_detection(f'data/images/{uploaded_file.name}')
            st.image(res)
            st.balloons()
            print("完成")

    if is_hos == True:
        print("执行holistic")
        if st.button("开始"):
            res = holistic(f'data/images/{uploaded_file.name}')
            st.image(res)
            st.balloons()
            print("完成")

    if is_3D == True:
        print("执行3D检测")
        if st.button("开始"):
            res = detection_3d(f'data/images/{uploaded_file.name}', opt.model_name)
            st.image(res)
            st.balloons()
            print("完成")
    if is_chicun == True:
        print("执行检测")
        if st.button("开始"):
            res = biaoji(f'data/images/{uploaded_file.name}')
            st.image(res)
            st.balloons()
            print("完成")

    if is_area == True:
        print('执行检测')
        if st.button('开始'):
            img_res = area_compute(f'data/images/{uploaded_file.name}', opt.threshold1, opt.threshold2)[0]
            res = area_compute(f'data/images/{uploaded_file.name}', opt.threshold1, opt.threshold2)[1]
            pre_image = area_compute(f'data/images/{uploaded_file.name}', opt.threshold1, opt.threshold2)[2]
            # max_dil = area_compute(f'data/images/{uploaded_file.name}', opt.threshold1, opt.threshold2)[3]
            data_res = pd.DataFrame(res)
            st.write(data_res)
            # dil_res = pd.DataFrame(max_dil)
            # st.write(dil_res)
            st.image(img_res, caption="结果图展示")
            for i in range(len(pre_image)):
                st.image(pre_image[i], caption='轮廓%d' % i)
            st.balloons()
            print('识别完成')

    if is_maxdil == True:
        print('执行检测')
        if st.button('开始'):
            image_res = max_dil(f'data/images/{uploaded_file.name}', opt.threshold1, opt.threshold2)[0]
            da_res = max_dil(f'data/images/{uploaded_file.name}', opt.threshold1, opt.threshold2)[1]
            my_data = pd.DataFrame(da_res)
            st.write(my_data)
            st.image(image_res, caption="结果图展示")
            st.balloons()
            print('识别完成')
