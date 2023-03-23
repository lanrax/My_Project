# -*- coding: utf-8 -*-
import numpy as np
import urllib
import cv2
from uuid import uuid4


def yasuo(path, quality):
    img = cv2.imread(path)
    # '.jpg'表示把当前图片img按照jpg格式编码，按照不同格式编码的结果不一样
    img_encode = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, quality])[1]
    # imgg = cv2.imencode('.png', img)

    data_encode = np.array(img_encode)
    str_encode = data_encode.tostring()

    # 缓存数据保存到本地，以txt格式保存
    with open('../img_encode.txt', 'wb') as f:
        f.write(str_encode)
        f.flush

    with open('../img_encode.txt', 'rb') as f:
        str_encode = f.read()

    nparr = np.fromstring(str_encode, np.uint8)
    img_decode = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    images = "/home/hadoop/yolov5_streamlit_fina/streamlit_main/runs/yasuo_images/" + ''.join(str(uuid4()).split('-')) + '.jpeg'
    cv2.imwrite(images, img_decode)
    return images


    # cv2.imshow("img_decode", img_decode)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
