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
    picture_path = serializers.CharField()


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


class DetectSerializer(serializers.Serializer):
    picture_id = serializers.CharField(max_length=255, default="11")
    picture_path = serializers.CharField()
    engine = serializers.CharField(max_length=255, default="Pytorch")
    cls_top = serializers.CharField(max_length=255, default="50%")
    task_type = serializers.CharField(max_length=255, default="FireDetect")

    def create(self, validated_data):
        return Detect.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.picture_id = validated_data.get('picture_id', instance.picture_id)
        instance.picture_path = validated_data.get('picture_path', instance.picture_path)
        instance.engine = validated_data.get('engine', instance.engine)
        instance.cls_top = validated_data.get('cls_top', instance.cls_top)
        instance.task_type = validated_data.get('task_type', instance.task_type)
        instance.save()
        return instance


class DetectResultSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255, default="11")
    conclusion = serializers.CharField(max_length=255, default="True")
    x_min = serializers.CharField(max_length=255, default="0")
    y_min = serializers.CharField(max_length=255, default="0")
    x_max = serializers.CharField(max_length=255, default="0")
    y_max = serializers.CharField(max_length=255, default="0")
    name = serializers.CharField(max_length=255, default="cat")
    confidence = serializers.CharField(max_length=255, default="1")

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.conclusion = validated_data.get('conclusion', instance.conclusion)
        instance.x_min = validated_data.get('x_min', instance.x_min)
        instance.y_min = validated_data.get('y_min', instance.y_min)
        instance.x_max = validated_data.get('x_max', instance.x_max)
        instance.y_max = validated_data.get('y_max', instance.y_max)
        instance.name = validated_data.get('name', instance.name)
        instance.confidence = validated_data.get('confidence', instance.confidence)
        instance.save()
        return instance
