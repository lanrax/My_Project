import base64
import json
import os

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.viewsets import GenericViewSet

from eyedetected.eye import httpRequest
from eyedetected.eye.models import Result, Picture
from eyedetected.eye.serializers import SyncSerializer, ResultSerializer
from eyedetected.eye.views_origin import detect_url_select
from eyedetected.settings import PIC_URL


def Transdata(transdata):
    imgdata = base64.b64decode(transdata["picture_path"])
    file = open("./pic/" + transdata["picture_id"] + '.jpg', 'wb')
    file.write(imgdata)
    return transdata['picture_id']


def DeletePic(delete_data):
    print("./pic/" + delete_data + '.jpg')
    os.remove("./pic/" + delete_data + '.jpg')
    return 'ok'


def Ret(message, data, delete_data):
    list(map(DeletePic, delete_data))
    if message != "":
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": message,
                         "data": ""})
    else:
        return Response({"status": status.HTTP_200_OK, "message": "success",
                         "data": data})


class FireDetectBaseGenericViewSets(GenericViewSet):

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = SyncSerializer(data=data)
        paths = []
        pic_RetDate = []
        if serializer.is_valid():
            for x in serializer.data["assignment"]:
                is_exist = Picture.objects.filter(picture_name=x["picture_id"])
                if len(is_exist) != 0:
                    return Ret('Duplicate image id', '', [])
            result_list = list(map(Transdata, serializer.data["assignment"]))
            ids = result_list
            for i in range(len(ids)):
                url = PIC_URL + ids[i] + ".jpg"
                paths.append(url)
            for id_num in range(len(ids)):
                Picture.objects.create(picture_name=ids[id_num], path=paths[id_num], task=0)
            detect_data = httpRequest.postDetect(detect_url_select("fire_url"), paths, ids)
            detect_json = json.loads(detect_data)
            if detect_data is None or detect_data == "" or detect_json["status"] != 200:
                if detect_json["status"] == 203:
                    return Ret('URL is error', '', ids)
                return Ret('detect failed', '', ids)
            result_serializer = ResultSerializer(data=detect_json["result"], many=True)
            result_serializer.is_valid(raise_exception=True)
            result_serializer.save()
            for pic_num in range(len(ids)):
                pic_RetBody = {}
                pic_Result = []
                result = Result.objects.filter(picture_name_id=ids[pic_num]).filter(Q(name="fire") | Q(name="smoke"))
                pic_RetBody['picture_id'] = ids[pic_num]
                pic_RetBody['conclusion'] = True
                if len(result) != 0:
                    for resultNum in range(len(result)):
                        pic_coordinate = {'x_min': result[resultNum].x_min, 'y_min': result[resultNum].y_min,
                                          'x_max': result[resultNum].x_max, 'y_max': result[resultNum].y_max,
                                          'confidence': result[resultNum].confidence,
                                          'name': result[resultNum].name}
                        pic_Result.append(pic_coordinate)
                else:
                    pic_RetBody['conclusion'] = False
                pic_RetBody['coordinate'] = pic_Result
                pic_RetDate.append(pic_RetBody)
            return Ret('', pic_RetDate, ids)
        return Ret('request error', '', [])


class FireInfraredBaseGenericViewSets(GenericViewSet):

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = SyncSerializer(data=data)
        paths = []
        pic_RetDate = []
        if serializer.is_valid():
            for x in serializer.data["assignment"]:
                is_exist = Picture.objects.filter(picture_name=x["picture_id"])
                if len(is_exist) != 0:
                    return Ret('Duplicate image id', '', [])
            result_list = list(map(Transdata, serializer.data["assignment"]))
            ids = result_list
            for i in range(len(ids)):
                url = PIC_URL + ids[i] + ".jpg"
                paths.append(url)
            for id_num in range(len(ids)):
                Picture.objects.create(picture_name=ids[id_num], path=paths[id_num], task=1)
            detect_data = httpRequest.postDetect(detect_url_select("fire_infrared_url"), paths, ids)
            detect_json = json.loads(detect_data)
            if detect_data is None or detect_data == "" or detect_json["status"] != 200:
                if detect_json["status"] == 203:
                    return Ret('URL is error', '', ids)
                return Ret('detect failed', '', ids)
            resultserlizer = ResultSerializer(data=detect_json["result"], many=True)
            resultserlizer.is_valid(raise_exception=True)
            resultserlizer.save()
            for pic_num in range(len(ids)):
                result = Result.objects.filter(picture_name_id=ids[pic_num]).filter(Q(name="fire") | Q(name="smoke"))
                pic_RetBody = {}
                pic_Result = []
                pic_RetBody['picture_id'] = ids[pic_num]
                pic_RetBody['conclusion'] = True
                if len(result) != 0:
                    for resultNum in range(len(result)):
                        pic_coordinate = {'x_min': result[resultNum].x_min, 'y_min': result[resultNum].y_min,
                                          'x_max': result[resultNum].x_max, 'y_max': result[resultNum].y_max,
                                          'confidence': result[resultNum].confidence,
                                          'name': result[resultNum].name}
                        pic_Result.append(pic_coordinate)
                else:
                    pic_RetBody['conclusion'] = False
                pic_RetBody['coordinate'] = pic_Result
                pic_RetDate.append(pic_RetBody)
            return Ret('', pic_RetDate, ids)
        return Ret('request error', '', [])


# InvasionBaseDetectGenericViewSets 入侵检测
class InvasionBaseDetectGenericViewSets(GenericViewSet):

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = SyncSerializer(data=data)
        paths = []
        pic_RetDate = []
        if serializer.is_valid():
            for x in serializer.data["assignment"]:
                is_exist = Picture.objects.filter(picture_name=x["picture_id"])
                if len(is_exist) != 0:
                    return Ret('Duplicate image id', '', [])
            result_list = list(map(Transdata, serializer.data["assignment"]))
            ids = result_list
            for i in range(len(ids)):
                url = PIC_URL + ids[i] + ".jpg"
                paths.append(url)
            for id_num in range(len(ids)):
                Picture.objects.create(picture_name=ids[id_num], path=paths[id_num], task=2)
            detect_data = httpRequest.postDetect(detect_url_select("person_url"), paths, ids)
            detect_json = json.loads(detect_data)
            if detect_data is None or detect_data == "" or detect_json["status"] != 200:
                if detect_json["status"] == 203:
                    return Ret('URL is error', '', ids)
                return Ret('detect failed', '', ids)
            resultserlizer = ResultSerializer(data=detect_json["result"], many=True)
            resultserlizer.is_valid(raise_exception=True)
            resultserlizer.save()
            for pic_num in range(len(ids)):
                pic_RetBody = {}
                result = Result.objects.filter(picture_name_id=ids[pic_num]).filter(name="person")
                pic_RetBody['picture_id'] = ids[pic_num]
                pic_Result = []
                if len(result) != 0:
                    pic_RetBody['conclusion'] = True
                    for resultNum in range(len(result)):
                        pic_coordinate = {'x_min': result[resultNum].x_min, 'y_min': result[resultNum].y_min,
                                          'x_max': result[resultNum].x_max, 'y_max': result[resultNum].y_max,
                                          'confidence': result[resultNum].confidence,
                                          'name': result[resultNum].name}
                        pic_Result.append(pic_coordinate)
                else:
                    pic_RetBody['conclusion'] = False
                pic_RetBody['coordinate'] = pic_Result
                pic_RetDate.append(pic_RetBody)
            return Ret('', pic_RetDate, ids)
        return Ret('request error', '', [])


# InvasionInfraredBaseDetectGenericViewSets 红外入侵检测
class InvasionInfraredBaseDetectGenericViewSets(GenericViewSet):

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = SyncSerializer(data=data)
        paths = []
        pic_RetDate = []
        if serializer.is_valid():
            for x in serializer.data["assignment"]:
                is_exist = Picture.objects.filter(picture_name=x["picture_id"])
                if len(is_exist) != 0:
                    return Ret('Duplicate image id', '', [])
            result_list = list(map(Transdata, serializer.data["assignment"]))
            ids = result_list
            for i in range(len(ids)):
                url = PIC_URL + ids[i] + ".jpg"
                paths.append(url)
            for id_num in range(len(ids)):
                Picture.objects.create(picture_name=ids[id_num], path=paths[id_num], task=3)
            detect_data = httpRequest.postDetect(detect_url_select("person_infrared_url"), paths, ids)
            detect_json = json.loads(detect_data)
            if detect_data is None or detect_data == "" or detect_json["status"] != 200:
                if detect_json["status"] == 203:
                    return Ret('URL is error', '', ids)
                return Ret('detect failed', '', ids)
            resultserlizer = ResultSerializer(data=detect_json["result"], many=True)
            resultserlizer.is_valid(raise_exception=True)
            resultserlizer.save()
            for pic_num in range(len(ids)):
                pic_RetBody = {}
                pic_Result = []
                result = Result.objects.filter(picture_name_id=ids[pic_num]).filter(name="person")
                pic_RetBody['picture_id'] = ids[pic_num]
                pic_RetBody['conclusion'] = True
                if len(result) != 0:
                    for resultNum in range(len(result)):
                        pic_coordinate = {'x_min': result[resultNum].x_min, 'y_min': result[resultNum].y_min,
                                          'x_max': result[resultNum].x_max, 'y_max': result[resultNum].y_max,
                                          'confidence': result[resultNum].confidence,
                                          'name': result[resultNum].name}
                        pic_Result.append(pic_coordinate)
                else:
                    pic_RetBody['conclusion'] = False
                pic_RetBody['coordinate'] = pic_Result
                pic_RetDate.append(pic_RetBody)
            return Ret('', pic_RetDate, ids)
        return Ret('request error', '', [])


# CrowdBaseDetectGenericViewSets 人群密度检测
class CrowdBaseDetectGenericViewSets(GenericViewSet):

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = SyncSerializer(data=data)
        paths = []
        pic_RetDate = []
        if serializer.is_valid():
            for x in serializer.data["assignment"]:
                is_exist = Picture.objects.filter(picture_name=x["picture_id"])
                if len(is_exist) != 0:
                    return Ret('Duplicate image id', '', [])
            result_list = list(map(Transdata, serializer.data["assignment"]))
            ids = result_list
            for i in range(len(ids)):
                url = PIC_URL + ids[i] + ".jpg"
                paths.append(url)
            for id_num in range(len(ids)):
                Picture.objects.create(picture_name=ids[id_num], path=paths[id_num], task=4)
            detect_data = httpRequest.postDetect(detect_url_select("person_url"), paths, ids)
            detect_json = json.loads(detect_data)
            if detect_data is None or detect_data == "" or detect_json["status"] != 200:
                if detect_json["status"] == 203:
                    return Ret('URL is error', '', ids)
                return Ret('detect failed', '', ids)
            resultserlizer = ResultSerializer(data=detect_json["result"], many=True)
            resultserlizer.is_valid(raise_exception=True)
            resultserlizer.save()
            for pic_num in range(len(ids)):
                pic_RetBody = {}
                result = Result.objects.filter(picture_name_id=ids[pic_num]).filter(name="person")
                pic_RetBody['picture_id'] = ids[pic_num]
                pic_RetBody['conclusion'] = str(len(result))
                pic_Result = []
                if len(result) != 0:
                    for resultNum in range(len(result)):
                        pic_coordinate = {'x_min': result[resultNum].x_min, 'y_min': result[resultNum].y_min,
                                          'x_max': result[resultNum].x_max, 'y_max': result[resultNum].y_max,
                                          'confidence': result[resultNum].confidence,
                                          'name': result[resultNum].name}
                        pic_Result.append(pic_coordinate)
                pic_RetBody['coordinate'] = pic_Result
                pic_RetDate.append(pic_RetBody)
            return Ret('', pic_RetDate, ids)
        return Ret('request error', '', [])


# CrowdInfraredBaseDetectGenericViewSets 人群密度红外检测
class CrowdInfraredBaseDetectGenericViewSets(GenericViewSet):

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = SyncSerializer(data=data)
        paths = []
        pic_RetDate = []
        if serializer.is_valid():
            for x in serializer.data["assignment"]:
                is_exist = Picture.objects.filter(picture_name=x["picture_id"])
                if len(is_exist) != 0:
                    return Ret('Duplicate image id', '', [])
            result_list = list(map(Transdata, serializer.data["assignment"]))
            ids = result_list
            for i in range(len(ids)):
                url = PIC_URL + ids[i] + ".jpg"
                paths.append(url)
            for id_num in range(len(ids)):
                Picture.objects.create(picture_name=ids[id_num], path=paths[id_num], task=5)
            detect_data = httpRequest.postDetect(detect_url_select("person_infrared_url"), paths, ids)
            detect_json = json.loads(detect_data)
            if detect_data is None or detect_data == "" or detect_json["status"] != 200:
                if detect_json["status"] == 203:
                    return Ret('URL is error', '', ids)
                return Ret('detect failed', '', ids)
            resultserlizer = ResultSerializer(data=detect_json["result"], many=True)
            resultserlizer.is_valid(raise_exception=True)
            resultserlizer.save()
            for pic_num in range(len(ids)):
                pic_RetBody = {}
                result = Result.objects.filter(picture_name_id=ids[pic_num]).filter(name="person")
                pic_RetBody['picture_id'] = ids[pic_num]
                pic_RetBody['conclusion'] = str(len(result))
                if len(result) != 0:
                    pic_Result = []
                    for resultNum in range(len(result)):
                        pic_coordinate = {'x_min': result[resultNum].x_min, 'y_min': result[resultNum].y_min,
                                          'x_max': result[resultNum].x_max, 'y_max': result[resultNum].y_max,
                                          'confidence': result[resultNum].confidence,
                                          'name': result[resultNum].name}
                        pic_Result.append(pic_coordinate)
                    pic_RetBody['coordinate'] = pic_Result
                    pic_RetDate.append(pic_RetBody)
                else:
                    pic_RetDate.append(pic_RetBody)
            return Ret('', pic_RetDate, ids)
        return Ret('request error', '', [])
