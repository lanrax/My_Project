import cv2
import imutils
import numpy as np
from imutils import contours
from uuid import uuid4


def area_compute(img_path, threshold1, threshold2):
    # 1.导入图片
    img_src = cv2.imread(img_path)

    # 2.灰度化
    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    # 此处应加入滤波函数
    img_gray = cv2.GaussianBlur(img_gray, (9, 9), 0)
    """
    这里cv2前面必须要有变量接收，因为  cv2.GaussianBlur(img_gray, (9, 9), 0) 虽然不会报错，但是图片其实没有经过高斯滤波处理
    """

    img_res = cv2.Canny(img_gray, threshold1, threshold2)
    """
    如果边缘像素点梯度值大于高阈值，则被认为是强边缘点。如果边缘梯度值小于高阈值，大于低阈值，则标记为弱边缘点。小于低阈值的点则被抑制掉。
    """

    img_bin = cv2.dilate(img_res, None, iterations=1)
    img_bin = cv2.erode(img_bin, None, iterations=1)

    # 3.连通域分析
    cnts = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)  # 返回cnts中的轮廓

    # Sort contours from left to right as leftmost contour is reference object
    contours.sort_contours(cnts)  # 对得到的轮廓进行升序排序

    # Remove contours which are not large enough
    cnts = [x for x in cnts if cv2.contourArea(x) > 100]  # 只保留轮廓数字大于100的
    # mask = np.zeros(img_gray.shape, np.uint8)
    # mask = cv2.drawContours(mask, cnts, -1, 255, -1)


    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img_gray, mask=mask)
    #
    # res_dil = []
    # res_dil.append("轮廓内的最大值： %d" % max_val)
    # res_dil.append("轮廓内最大值的坐标： (%d, %d)" % max_loc)
    # 4.轮廓面积打印
    img_contours = []
    res = []
    img_imwrite = []
    cm_res = []
    fina_res = []
    for i in range(len(cnts)):
        area = cv2.contourArea(cnts[i])

        res.append("轮廓 %d 的像素面积是:%d" % (i, area))
        cm_res.append("轮廓 %d 的面积是:%d平方厘米" % (i, area // 146 ** 2))

        img_temp = np.zeros(img_src.shape, np.uint8)
        img_contours.append(img_temp)
        cv2.drawContours(img_contours[i], cnts, i, (0, 0, 255), 5)
        cv2.drawContours(img_src, cnts, -1, (0, 0, 255), 5)
        img_imwrite.append("/home/hadoop/yolov5_streamlit_fina/streamlit_main/runs/area_detect/" + str(i) + '.jpg')
        cv2.imwrite(img_imwrite[i], img_contours[i])
    fina_res.append(res)
    fina_res.append(cm_res)

    res_path = "/home/hadoop/yolov5_streamlit_fina/streamlit_main/runs/area_detect/" + ''.join(
        str(uuid4()).split('_')) + '.jpg'
    cv2.imwrite(res_path, img_src)

    return res_path, fina_res, img_imwrite

#
area_compute("/home/hadoop/yolov5_streamlit_fina/streamlit_main/data/images/tupian2.jpg", 50, 100)
# # #
