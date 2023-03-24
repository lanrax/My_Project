from django.db import models


class Picture(models.Model):
    picture_name = models.CharField(max_length=255, primary_key=True, blank=True, verbose_name="图片唯一名称")
    path = models.CharField(max_length=255, verbose_name="图片路径")
    task = models.PositiveIntegerField(verbose_name="任务类型")
    # 0:烟火检测,1:红外烟火检测,2:入侵检测,3:红外入侵检测,4:人群密度检测,5:人群密度红外检测
    recognition = models.PositiveIntegerField(verbose_name="认可度", null=True)  # 1:认可，2：勉强认可，3：不认可
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")


class Result(models.Model):
    x_min = models.CharField(max_length=255, verbose_name="坐标x最小值")
    y_min = models.CharField(max_length=255, verbose_name="坐标y最小值")
    x_max = models.CharField(max_length=255, verbose_name="坐标x最大值")
    y_max = models.CharField(max_length=255, verbose_name="坐标y最大值")
    confidence = models.CharField(max_length=255, verbose_name="图片准确率")
    classno = models.IntegerField(verbose_name="识别类别")
    name = models.CharField(max_length=255, verbose_name="识别类别名称")
    picture_name = models.ForeignKey(Picture, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="图片唯一名称")
    update_time = models.DateField(auto_now=True, null=True, verbose_name="更新时间")
    create_time = models.DateField(auto_now_add=True, null=True, verbose_name="上传时间")


class DetectType(models.Model):
    detect_type = models.IntegerField(primary_key=True, verbose_name="检测类别")
    detect_describe = models.CharField(max_length=255, verbose_name="检测描述")


class Detect(models.Model):
    picture_name = models.ForeignKey(Picture, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="图片唯一名称")
    detect_type = models.ForeignKey(DetectType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="检测类别")
    task = models.CharField(max_length=255, null=True, verbose_name="图片任务")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")


class DetectServer(models.Model):
    detect_id = models.BigAutoField(primary_key=True)
    detect_name = models.CharField(max_length=255, blank=True, verbose_name="检测任务")
    detect_url = models.CharField(max_length=255, verbose_name="检测url")
