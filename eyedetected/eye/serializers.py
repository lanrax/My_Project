from django.contrib.auth.models import User, Group
from rest_framework import serializers

from eyedetected.eye.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class GaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


class TaskTypeSerializer(serializers.ListField):
    task_type = serializers.IntegerField()


class TaskUpSerializer(serializers.Serializer):
    picture_id = serializers.CharField(max_length=255)
    picture_path = serializers.CharField(max_length=255)
    task = TaskTypeSerializer()


class TaskListSerializer(serializers.Serializer):
    assignment = TaskUpSerializer(many=True)


class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['result', 'code', 'error']


class SyncSerializer(serializers.Serializer):
    picture_id = serializers.CharField(max_length=255)
    picture_path = serializers.CharField(max_length=255)


class SyncSerializer(serializers.Serializer):
    assignment = SyncSerializer(many=True)


class RecognizeSerializer(serializers.Serializer):
    picture_id = serializers.CharField(max_length=255)
    picture_recognition = serializers.IntegerField()


class RecognizesSerializer(serializers.Serializer):
    Recognize = RecognizeSerializer(many=True)


class DetectServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetectServer
        fields = "__all__"


class Retresult(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['x_min', 'y_min', 'x_max', 'y_max', 'confidence', 'name']


class RetBody(serializers.Serializer):
    picture_id = serializers.CharField(max_length=255)
    result = serializers.CharField(max_length=255)
    retResult = Retresult(many=True)


class RetData(serializers.Serializer):
    RetBody = RetBody(many=True)


class CreateURLSerializer(serializers.Serializer):
    detect_name = serializers.CharField(max_length=255)
    detect_url = serializers.CharField(max_length=255)


class CreateServiceSerializer(serializers.Serializer):
    detect_service = CreateURLSerializer(many=True)


class UpdateURLSerializer(serializers.Serializer):
    detect_id = serializers.CharField(max_length=255)
    detect_name = serializers.CharField(max_length=255)
    detect_url = serializers.CharField(max_length=255)


class UpdateServiceSerializer(serializers.Serializer):
    detect_service = UpdateURLSerializer(many=True)


class DeleteServiceSerializer(serializers.Serializer):
    detect_id = serializers.CharField(max_length=255)
