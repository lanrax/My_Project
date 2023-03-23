from django.conf import settings
from eyedetected.eye.serializers import DetectSerializer, DetectResultSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from eyedetected.eye.models import Picture, Result
import base64
from eyedetected.div_test import DecisionTree


def Transdata(transdata, number):
    """

    :param transdata: 传入的base64
    :param number:    图片id

    """
    imgdata = base64.b64decode(transdata)
    file = open("/home/hadoop/eme/eyedetected/uuid_pic/" + number + '.jpg', 'wb')  # 将转换后的图片保存在该路径
    file.write(imgdata)
    return file.name


class FireDetectView(APIView):
    def get(self, request):

        return Response("serializer.errors", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):

        serializer = DetectSerializer(data=request.data)  # 序列化传入的参数
        if serializer.is_valid():
            if serializer.data["task_type"] == "FireDetect":
                ser_res = DetectResultSerializer(data=request.data)
                images = Transdata(serializer.data["picture_path"], serializer.data["picture_id"])
                path_path = images
                # ******图片路径相关问题： 即现在只能放进去单张图片，无法批量检测传递相关参数**********
                img_res = DecisionTree().select_func(path_path, cls_top1=serializer.data["cls_top"],
                                                     engine=serializer.data["engine"],
                                                     task_type=serializer.data["task_type"])
                xyxy = DecisionTree().execute_func(img_res, file_path=path_path, engine=serializer.data["engine"])
                if ser_res.is_valid():
                    res = []  # 最后返回的结果保存在res中
                    for i in range(len(xyxy)):  # len(xyxy)为需要检测的目标个数
                        return_data = ser_res.data  # 向列表中append字典时，字典对象要在for循环或者方法内部实例化
                        return_data["id"] = serializer.data["picture_id"]
                        return_data["conclusion"] = "True"
                        return_data["x_min"] = xyxy[i][1]
                        return_data["y_min"] = xyxy[i][2]
                        return_data["x_max"] = xyxy[i][3]
                        return_data["y_max"] = xyxy[i][4]
                        return_data["confidence"] = xyxy[i][5]
                        return_data["name"] = xyxy[i][6]
                        res.append(return_data)  # 这里return_data的周期应该在for循环里，即在for里面实例化return_data

                    return Response(res, status=status.HTTP_201_CREATED)
            else:
                Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class FireInfraredBaseGenericViewSets(APIView):

    def get(self, request):

        return Response("serializer.errors", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):

        serializer = DetectSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.data["task_type"] == "FireInfraredDetect":
                ser_res = DetectResultSerializer(data=request.data)
                images = Transdata(serializer.data["picture_path"], serializer.data["picture_id"])
                path_path = images
                img_res = DecisionTree().select_func(path_path, cls_top1=serializer.data["cls_top"],
                                                     engine=serializer.data["engine"],
                                                     task_type=serializer.data["task_type"])
                xyxy = DecisionTree().execute_func(img_res, file_path=path_path, engine=serializer.data["engine"])
                if ser_res.is_valid():
                    res = []
                    for i in range(len(xyxy)):
                        return_data = ser_res.data
                        return_data["id"] = serializer.data["picture_id"]
                        return_data["conclusion"] = "True"
                        return_data["x_min"] = xyxy[i][1]
                        return_data["y_min"] = xyxy[i][2]
                        return_data["x_max"] = xyxy[i][3]
                        return_data["y_max"] = xyxy[i][4]
                        return_data["confidence"] = xyxy[i][5]
                        return_data["name"] = xyxy[i][6]
                        res.append(return_data)

                    return Response(res, status=status.HTTP_201_CREATED)
            else:
                Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class InvasionBaseDetectGenericViewSets(APIView):

    def get(self, request):

        return Response("serializer.errors", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):

        serializer = DetectSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.data["task_type"] == "InvasionDetect":
                ser_res = DetectResultSerializer(data=request.data)
                images = Transdata(serializer.data["picture_path"], serializer.data["picture_id"])
                path_path = images
                img_res = DecisionTree().select_func(path_path, cls_top1=serializer.data["cls_top"],
                                                     engine=serializer.data["engine"],
                                                     task_type=serializer.data["task_type"])
                xyxy = DecisionTree().execute_func(img_res, file_path=path_path, engine=serializer.data["engine"])
                if ser_res.is_valid():
                    res = []
                    for i in range(len(xyxy)):
                        return_data = ser_res.data
                        return_data["id"] = serializer.data["picture_id"]
                        return_data["conclusion"] = "True"
                        return_data["x_min"] = xyxy[i][1]
                        return_data["y_min"] = xyxy[i][2]
                        return_data["x_max"] = xyxy[i][3]
                        return_data["y_max"] = xyxy[i][4]
                        return_data["confidence"] = xyxy[i][5]
                        return_data["name"] = xyxy[i][6]
                        res.append(return_data)

                    return Response(res, status=status.HTTP_201_CREATED)
            else:
                Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class InvasionInfraredBaseDetectGenericViewSets(APIView):

    def get(self, request):

        return Response("serializer.errors", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):

        serializer = DetectSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.data["task_type"] == "InvasionInfraredDetect":
                ser_res = DetectResultSerializer(data=request.data)
                images = Transdata(serializer.data["picture_path"], serializer.data["picture_id"])
                path_path = images
                img_res = DecisionTree().select_func(path_path, cls_top1=serializer.data["cls_top"],
                                                     engine=serializer.data["engine"],
                                                     task_type=serializer.data["task_type"])
                xyxy = DecisionTree().execute_func(img_res, file_path=path_path, engine=serializer.data["engine"])
                if ser_res.is_valid():
                    res = []
                    for i in range(len(xyxy)):
                        return_data = ser_res.data
                        return_data["id"] = serializer.data["picture_id"]
                        return_data["conclusion"] = "True"
                        return_data["x_min"] = xyxy[i][1]
                        return_data["y_min"] = xyxy[i][2]
                        return_data["x_max"] = xyxy[i][3]
                        return_data["y_max"] = xyxy[i][4]
                        return_data["confidence"] = xyxy[i][5]
                        return_data["name"] = xyxy[i][6]
                        res.append(return_data)

                    return Response(res, status=status.HTTP_201_CREATED)
            else:
                Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CrowdBaseDetectGenericViewSets(APIView):

    def get(self, request):

        return Response("serializer.errors", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):

        serializer = DetectSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.data["task_type"] == "CrowdDetect":
                ser_res = DetectResultSerializer(data=request.data)
                images = Transdata(serializer.data["picture_path"], serializer.data["picture_id"])
                path_path = images
                img_res = DecisionTree().select_func(path_path, cls_top1=serializer.data["cls_top"],
                                                     engine=serializer.data["engine"],
                                                     task_type=serializer.data["task_type"])
                xyxy = DecisionTree().execute_func(img_res, file_path=path_path, engine=serializer.data["engine"])
                if ser_res.is_valid():
                    res = []
                    for i in range(len(xyxy)):
                        return_data = ser_res.data
                        return_data["id"] = serializer.data["picture_id"]
                        return_data["conclusion"] = "True"
                        return_data["x_min"] = xyxy[i][1]
                        return_data["y_min"] = xyxy[i][2]
                        return_data["x_max"] = xyxy[i][3]
                        return_data["y_max"] = xyxy[i][4]
                        return_data["confidence"] = xyxy[i][5]
                        return_data["name"] = xyxy[i][6]
                        res.append(return_data)

                    return Response(res, status=status.HTTP_201_CREATED)
            else:
                Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CrowdInfraredBaseDetectGenericViewSets(APIView):

    def get(self, request):

        return Response("serializer.errors", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):

        serializer = DetectSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.data["task_type"] == "CrowdInfraredDetect":
                ser_res = DetectResultSerializer(data=request.data)
                images = Transdata(serializer.data["picture_path"], serializer.data["picture_id"])
                path_path = images
                img_res = DecisionTree().select_func(path_path, cls_top1=serializer.data["cls_top"],
                                                     engine=serializer.data["engine"],
                                                     task_type=serializer.data["task_type"])
                xyxy = DecisionTree().execute_func(img_res, file_path=path_path, engine=serializer.data["engine"])
                if ser_res.is_valid():
                    res = []
                    for i in range(len(xyxy)):
                        return_data = ser_res.data
                        return_data["id"] = serializer.data["picture_id"]
                        return_data["conclusion"] = "True"
                        return_data["x_min"] = xyxy[i][1]
                        return_data["y_min"] = xyxy[i][2]
                        return_data["x_max"] = xyxy[i][3]
                        return_data["y_max"] = xyxy[i][4]
                        return_data["confidence"] = xyxy[i][5]
                        return_data["name"] = xyxy[i][6]
                        res.append(return_data)

                    return Response(res, status=status.HTTP_201_CREATED)
            else:
                Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
