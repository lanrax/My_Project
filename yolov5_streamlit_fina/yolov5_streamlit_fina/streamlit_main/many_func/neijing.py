import cv2
import numpy as np
from imutils import contours
import imutils
from uuid import uuid4
import math


# ***** 求两点间距离*****
def getDist_P2P(Point0, PointA):
    distance = math.pow((Point0[0] - PointA[0]), 2) + math.pow((Point0[1] - PointA[1]), 2)
    distance = math.sqrt(distance)
    return distance


def get_contour(img, t1, t2):
    """获取连通域


    :param img: 输入图片
    :return: 最大连通域

    """

    # 2.灰度化
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 此处应加入滤波函数
    img_gray = cv2.GaussianBlur(img_gray, (9, 9), 0)
    """
    这里cv2前面必须要有变量接收，因为  cv2.GaussianBlur(img_gray, (9, 9), 0) 虽然不会报错，但是图片其实没有经过高斯滤波处理
    """

    img_res = cv2.Canny(img_gray, t1, t2)
    """
    如果边缘像素点梯度值大于高阈值，则被认为是强边缘点。如果边缘梯度值小于高阈值，大于低阈值，则标记为弱边缘点。小于低阈值的点则被抑制掉。
    """

    img_bin = cv2.dilate(img_res, None, iterations=1)
    img_bin = cv2.erode(img_bin, None, iterations=1)
    # 灰度化, 二值化, 连通域分析
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, img_res = cv2.threshold(img_bin, 127, 255, cv2.THRESH_BINARY)

    cnts = cv2.findContours(img_res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    contours.sort_contours(cnts)
    cnts = [x for x in cnts if cv2.contourArea(x) > 100]

    return img_gray, cnts[0]


def max_dil(img_path, t1, t2):
    # 1.导入图片
    res = []
    img_src = cv2.imread(img_path)

    # 2.获取连通域

    img_gray, contour = get_contour(img_src, t1, t2)

    # 3.轮廓外边缘点
    mask = np.zeros(img_gray.shape, np.uint8)
    mask = cv2.drawContours(mask, [contour], -1, 255, -1)
    left_most = tuple(contour[contour[:, :, 0].argmin()][0])  # 是取三维矩阵中第一维的所有数据
    right_most = tuple(contour[contour[:, :, 0].argmax()][0])
    top_most = tuple(contour[contour[:, :, 1].argmin()][0])  # 是取三维矩阵中第二维的所有数据
    bottom_most = tuple(contour[contour[:, :, 1].argmax()][0])

    # print("left_most=", left_most)
    # print("right_most=", right_most)
    # print("top_most=", top_most)
    # print("bottom_most=", bottom_most)
    # print(getDist_P2P(left_most, bottom_most)//146)
    # print(getDist_P2P(right_most, bottom_most)//146)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img_src, "A", left_most, font, 1, (0, 0, 255), 2)
    cv2.putText(img_src, "B", right_most, font, 1, (0, 0, 255), 2)
    cv2.putText(img_src, "C", top_most, font, 1, (0, 0, 255), 2)
    cv2.putText(img_src, "D", bottom_most, font, 1, (0, 0, 255), 2)

    cv2.line(img_src, left_most, right_most, (0, 255, 0), 2)
    cv2.line(img_src, top_most, bottom_most, (0, 255, 0), 2)
    res.append("AB的长度：%d 厘米" % (getDist_P2P(left_most, right_most)/146))
    res.append("CD的长度：%d 厘米" % (getDist_P2P(top_most, bottom_most)/146))
    # 4.获取最小值,最大值, 最小值位置, 最大值位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img_gray, mask=mask)
    # print("min_val=", min_val)
    # print("轮廓内的最大值：", max_val)
    # print("min_loc=", min_loc)
    # print("轮廓内最大值的坐标：", max_loc)
    # 5.计算掩模区域图片
    # mask_ko = np.zeros(img_src.shape, np.uint8)
    # mask_ko = cv2.drawContours(mask_ko, [contour], -1, (255, 255, 255), -1)
    # img_loc = cv2.bitwise_and(img_src, mask_ko)

    # 6.显示图片

    cv2.imwrite("opencv.jpg", img_src)

    res_path = "/home/hadoop/yolov5_streamlit_fina/streamlit_main/runs/max_dilia" + ''.join(
        str(uuid4()).split('-')) + '.jpg'
    cv2.imwrite(res_path, img_src)
    return res_path, res

# if __name__ == '__main__':
#     max_dil("/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/images/tupian.jpg", 50, 100)
