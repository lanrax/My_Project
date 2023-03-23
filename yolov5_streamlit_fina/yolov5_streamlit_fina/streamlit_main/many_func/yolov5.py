import cv2
import torch
from PIL import Image
import os
import shutil

def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

def detect_2(image_path):
    # Model
    # model = torch.hub.load('/home/hadoop/yolov5','yolov5s.pt', source='local')
    model = torch.hub.load('/home/hadoop/yolov5_streamlit_fina/streamlit_main/yolov5', 'custom',
                           '/home/hadoop/yolov5_streamlit_fina/streamlit_main/weights/yolov5s.pt',
                           source='local')  # custom trained model

    # Images
    # for f in 'zidane.jpg', 'bus.jpg':
    #     torch.hub.download_url_to_file('https://ultralytics.com/images/' + f, f)  # download 2 images
    # im1 = Image.open('zidane.jpg')  # PIL image
    im2 = cv2.imread(image_path)[...,::-1]
    # OpenCV image (BGR to RGB)

    # Inference
    results = model([im2], size=640)  # batch of images
    del_file('/home/hadoop/yolov5_streamlit_fina/streamlit_main/runs/detect')
    results.save()  #
    # print("333",results)
    # print(results.pandas().xyxy[0])
    return results.pandas().xyxy[0]

# detect_2('/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/images/bus.jpg')
# Results
# results.print()
# results.save()  # or .show()
#
# results.xyxy[0]  # im1 predictions (tensor)
# results.pandas().xyxy[0]  # im1 predictions (pandas)
