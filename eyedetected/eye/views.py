import json
import random
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.viewsets import GenericViewSet
from eyedetected.eye import httpRequest
from eyedetected.eye.models import Result, Picture, DetectServer
from eyedetected.eye.serializers import SyncSerializer, ResultSerializer, PictureSerializer, RecognizesSerializer, \
    DetectServerSerializer, UpdateServiceSerializer, CreateServiceSerializer, DeleteServiceSerializer


# Create your views here.
def detect_url_select(detect_name):
    url_list = DetectServer.objects.filter(detect_name=detect_name)
    url = random.choice(url_list)
    return url.detect_url


class DetectURLGenericViewSets(GenericViewSet):
    queryset = DetectServer.objects.all()
    serializer_class = DetectServerSerializer

    def list(self, request):
        instance = self.get_queryset()
        seiralizer = self.get_serializer(instance=instance, many=True)
        return Response(data=seiralizer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = CreateServiceSerializer(data=data)
        if serializer.is_valid():
            for x in serializer.data["detect_service"]:
                data_save = DetectServer.objects.create(detect_name=x["detect_name"],
                                                        detect_url=x["detect_url"]
                                                        )
                data_save.save()
            return Response({"status": status.HTTP_200_OK, "message": 'success', "data": "success"})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": 'failed', "data": "failed"})

    def update(self, request):
        data = JSONParser().parse(request)
        serializer = UpdateServiceSerializer(data=data)
        if serializer.is_valid():
            for x in serializer.data["detect_service"]:
                Server_data = DetectServer.objects.get(detect_id=x['detect_id'])
                Server_data.detect_url = x['detect_url']
                Server_data.detect_name = x['detect_name']
                Server_data.save()
            return Response({"status": status.HTTP_200_OK, "message": 'success', "data": "success"})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": 'failed', "data": "failed"})

    def delete(self, request):
        data = JSONParser().parse(request)
        serializer = DeleteServiceSerializer(data=data)
        if serializer.is_valid():
            id = serializer.data['detect_id']
            Server_data = DetectServer.objects.get(detect_id=id)
            Server_data.delete()
            return Response({"status": status.HTTP_200_OK, "message": 'success', "data": "success"})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": 'failed', "data": "failed"})


# FireDetectGenericViewSets 烟火检测
class FireDetectGenericViewSets(GenericViewSet):
    queryset = Result.objects.all()
    queryset = queryset.filter(Q(name="fire") | Q(name="smoke"))
    serializer_class = ResultSerializer

    def list(self, request):
        instance = self.get_queryset()
        seiralizer = self.get_serializer(instance=instance, many=True)
        return Response(data=seiralizer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pid):
        query_all = Result.objects.filter(picture_name_id=pid)
        serializer = ResultSerializer(query_all, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = SyncSerializer(data=data)
        ids = []
        paths = []
        pic_RetDate = []
        if serializer.is_valid():
            for x in serializer.data["assignment"]:
                is_exist = Picture.objects.filter(picture_name=x["picture_id"])
                if len(is_exist) != 0:
                    return Response({"status": status.HTTP_400_BAD_REQUEST, "message": 'Duplicate image id',
                                     "data": pic_RetDate})
                ids.append(x["picture_id"])
                paths.append(x["picture_path"])
            for id_num in range(len(ids)):
                Picture.objects.create(picture_name=ids[id_num], path=paths[id_num], task=0)
            detect_data = httpRequest.postDetect(detect_url_select("fire_url"), paths, ids)
            detect_json = json.loads(detect_data)
            if detect_data is None or detect_data == "" or detect_json["status"] != 200:
                if detect_json["status"] == 203:
                    return Response(
                        {"status": status.HTTP_400_BAD_REQUEST, "message": 'URL is error', "data": ""})
                return Response(
                    {"status": status.HTTP_400_BAD_REQUEST, "message": 'detect failed', "data": pic_RetDate})
            resultserlizer = ResultSerializer(data=detect_json["result"], many=True)
            resultserlizer.is_valid(raise_exception=True)
            resultserlizer.save()
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
            return Response({"status": status.HTTP_200_OK, "message": 'success', "data": pic_RetDate})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": 'request error', "data": pic_RetDate})


# FireInfraredDetectGenericViewSets 红外烟火检测
class FireInfraredDetectGenericViewSets(GenericViewSet):
    queryset = Result.objects.all()
    queryset = queryset.filter(Q(name="fire") | Q(name="smoke"))
    serializer_class = ResultSerializer

    def list(self, request):
        instance = self.get_queryset()
        seiralizer = self.get_serializer(instance=instance, many=True)
        return Response(data=seiralizer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = SyncSerializer(data=data)
        ids = []
        paths = []
        pic_RetDate = []
        if serializer.is_valid():
            for x in serializer.data["assignment"]:
                is_exist = Picture.objects.filter(picture_name=x["picture_id"])
                if len(is_exist) != 0:
                    return Response(
                        {"status": status.HTTP_400_BAD_REQUEST, "message": 'Duplicate image id',
                         "data": pic_RetDate})
                ids.append(x["picture_id"])
                paths.append(x["picture_path"])
            for id_num in range(len(ids)):
                Picture.objects.create(picture_name=ids[id_num], path=paths[id_num], task=1)
            detect_data = httpRequest.postDetect(detect_url_select("fire_infrared_url"), paths, ids)
            detect_json = json.loads(detect_data)
            if detect_data is None or detect_data == "" or detect_json["status"] != 200:
                if detect_json["status"] == 203:
                    return Response(
                        {"status": status.HTTP_400_BAD_REQUEST, "message": 'URL is error', "data": ""})
                return Response(
                    {"status": status.HTTP_400_BAD_REQUEST, "message": 'detect failed', "data": pic_RetDate})
            resultserlizer = ResultSerializer(data=detect_json["result"], many=True)
            resultserlizer.is_valid(raise_exception=True)
            resultserlizer.save()
            for pic_num in range(len(ids)):
                result = Result.objects.filter(picture_name_id=ids[pic_num]).filter(
                    Q(name="fire") | Q(name="smoke"))
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
            return Response({"status": status.HTTP_200_OK, "message": 'success', "data": pic_RetDate})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": 'request error', "data": pic_RetDate})


# InvasionDetectGenericViewSets 入侵检测
class InvasionDetectGenericViewSets(GenericViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def list(self, request):
        instance = self.get_queryset()
        seiralizer = self.get_serializer(instance=instance, many=True)
        return Response(data=seiralizer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = SyncSerializer(data=data)
        ids = []
        paths = []
        pic_RetDate = []
        if serializer.is_valid():
            for x in serializer.data["assignment"]:
                is_exist = Picture.objects.filter(picture_name=x["picture_id"])
                if len(is_exist) != 0:
                    return Response(
                        {"status": status.HTTP_400_BAD_REQUEST, "message": 'Duplicate image id',
                         "data": pic_RetDate})
                ids.append(x["picture_id"])
                paths.append(x["picture_path"])
            for id_num in range(len(ids)):
                Picture.objects.create(picture_name=ids[id_num], path=paths[id_num], task=2)
            detect_data = httpRequest.postDetect(detect_url_select("person_url"), paths, ids)
            detect_json = json.loads(detect_data)
            if detect_data is None or detect_data == "" or detect_json["status"] != 200:
                if detect_json["status"] == 203:
                    return Response(
                        {"status": status.HTTP_400_BAD_REQUEST, "message": 'URL is error', "data": ""})
                return Response(
                    {"status": status.HTTP_400_BAD_REQUEST, "message": 'detect failed', "data": pic_RetDate})
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
            return Response({"status": status.HTTP_200_OK, "message": 'success', "data": pic_RetDate})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": 'request error', "data": pic_RetDate})


# InvasionInfraredDetectGenericViewSets 红外入侵检测
class InvasionInfraredDetectGenericViewSets(GenericViewSet):
    queryset = Result.objects.all()
    queryset = queryset.filter(name="person")
    serializer_class = ResultSerializer

    def list(self, request):
        instance = self.get_queryset()
        seiralizer = self.get_serializer(instance=instance, many=True)
        return Response(data=seiralizer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = SyncSerializer(data=data)
        ids = []
        paths = []
        pic_RetDate = []
        if serializer.is_valid():
            for x in serializer.data["assignment"]:
                is_exist = Picture.objects.filter(picture_name=x["picture_id"])
                if len(is_exist) != 0:
                    return Response({"status": status.HTTP_400_BAD_REQUEST, "message": 'Duplicate image id',
                                     "data": pic_RetDate})
                ids.append(x["picture_id"])
                paths.append(x["picture_path"])
            for id_num in range(len(ids)):
                Picture.objects.create(picture_name=ids[id_num], path=paths[id_num], task=3)
            detect_data = httpRequest.postDetect(detect_url_select("person_infrared_url"), paths, ids)
            detect_json = json.loads(detect_data)
            if detect_data is None or detect_data == "" or detect_json["status"] != 200:
                if detect_json["status"] == 203:
                    return Response(
                        {"status": status.HTTP_400_BAD_REQUEST, "message": 'URL is error', "data": ""})
                return Response(
                    {"status": status.HTTP_400_BAD_REQUEST, "message": 'detect failed', "data": pic_RetDate})
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
            return Response({"status": status.HTTP_200_OK, "message": 'success', "data": pic_RetDate})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": 'request error', "data": pic_RetDate})


# CrowdDetectGenericViewSets 人群密度检测
class CrowdDetectGenericViewSets(GenericViewSet):
    queryset = Result.objects.all()
    queryset = queryset.filter(name="person")
    serializer_class = ResultSerializer

    def list(self, request):
        instance = self.get_queryset()
        seiralizer = self.get_serializer(instance=instance, many=True)
        return Response(data=seiralizer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = SyncSerializer(data=data)
        ids = []
        paths = []
        pic_RetDate = []
        if serializer.is_valid():
            for x in serializer.data["assignment"]:
                is_exist = Picture.objects.filter(picture_name=x["picture_id"])
                if len(is_exist) != 0:
                    return Response({"status": status.HTTP_400_BAD_REQUEST, "message": 'Duplicate image id',
                                     "data": pic_RetDate})
                ids.append(x["picture_id"])
                paths.append(x["picture_path"])
            for id_num in range(len(ids)):
                Picture.objects.create(picture_name=ids[id_num], path=paths[id_num], task=4)
            detect_data = httpRequest.postDetect(detect_url_select("person_url"), paths, ids)
            detect_json = json.loads(detect_data)
            if detect_data is None or detect_data == "" or detect_json["status"] != 200:
                if detect_json["status"] == 203:
                    return Response(
                        {"status": status.HTTP_400_BAD_REQUEST, "message": 'URL is error', "data": ""})
                return Response(
                    {"status": status.HTTP_400_BAD_REQUEST, "message": 'detect failed', "data": pic_RetDate})
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
            return Response({"status": status.HTTP_200_OK, "message": 'success', "data": pic_RetDate})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": 'request error', "data": pic_RetDate})


# CrowdInfraredDetectGenericViewSets 人群密度红外检测
class CrowdInfraredDetectGenericViewSets(GenericViewSet):
    queryset = Result.objects.all()
    queryset = queryset.filter(name="person")
    serializer_class = ResultSerializer

    def list(self, request):
        instance = self.get_queryset()
        seiralizer = self.get_serializer(instance=instance, many=True)
        return Response(data=seiralizer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = SyncSerializer(data=data)
        ids = []
        paths = []
        pic_RetDate = []
        if serializer.is_valid():
            for x in serializer.data["assignment"]:
                is_exist = Picture.objects.filter(picture_name=x["picture_id"])
                if len(is_exist) != 0:
                    return Response(
                        {"status": status.HTTP_400_BAD_REQUEST, "message": 'Duplicate image id',
                         "data": pic_RetDate})
                ids.append(x["picture_id"])
                paths.append(x["picture_path"])
            for id_num in range(len(ids)):
                Picture.objects.create(picture_name=ids[id_num], path=paths[id_num], task=5)
            detect_data = httpRequest.postDetect(detect_url_select("person_infrared_url"), paths, ids)
            detect_json = json.loads(detect_data)
            if detect_data is None or detect_data == "" or detect_json["status"] != 200:
                if detect_json["status"] == 203:
                    return Response(
                        {"status": status.HTTP_400_BAD_REQUEST, "message": 'URL is error', "data": ""})
                return Response(
                    {"status": status.HTTP_400_BAD_REQUEST, "message": 'detect failed', "data": pic_RetDate})
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
            return Response({"status": status.HTTP_200_OK, "message": 'success', "data": pic_RetDate})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": 'request error', "data": pic_RetDate})


# RecognizeGenericViewSets 认可度
class RecognizeGenericViewSets(GenericViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def list(self, request):
        instance = self.get_queryset()
        seiralizer = self.get_serializer(instance=instance, many=True)
        return Response(data=seiralizer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = RecognizesSerializer(data=data)
        if serializer.is_valid():
            for x in serializer.data["Recognize"]:
                picture_id = x["picture_id"]
                recognition = x["picture_recognition"]
                is_exist = Picture.objects.filter(picture_name=picture_id).count()
                if is_exist == 0:
                    return Response({
                        "status": status.HTTP_400_BAD_REQUEST, "message": 'pic_id is not found',
                        "data": {'result': False}})
                pic = Picture.objects.get(picture_name=picture_id)
                pic.recognition = recognition
                ret = pic.save()
                if ret is False:
                    return Response({
                        "status": status.HTTP_400_BAD_REQUEST, "message": 'Evaluation failed',
                        "data": {'result': False}})
                else:
                    return Response({"status": status.HTTP_200_OK, "message": 'success', "data": {'result': True}})
        return Response({"status": status.HTTP_200_OK, "message": 'success', "data": {'result': True}})
