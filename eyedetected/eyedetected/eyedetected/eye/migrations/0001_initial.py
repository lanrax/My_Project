# Generated by Django 4.1.3 on 2023-03-20 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cls_top', models.CharField(default='50%', max_length=255)),
                ('picture_id', models.CharField(default='id', max_length=255)),
                ('picture_path', models.TextField(default='base64')),
                ('engine', models.CharField(default='Pytorch', max_length=255, verbose_name='engine')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='DetectResult',
            fields=[
                ('id', models.CharField(default='0', max_length=255, primary_key=True, serialize=False)),
                ('conclusion', models.CharField(default='True', max_length=255, verbose_name='结论')),
                ('x_min', models.CharField(max_length=255, verbose_name='坐标x最小值')),
                ('y_min', models.CharField(max_length=255, verbose_name='坐标y最小值')),
                ('x_max', models.CharField(max_length=255, verbose_name='坐标x最大值')),
                ('y_max', models.CharField(max_length=255, verbose_name='坐标y最大值')),
                ('name', models.CharField(max_length=255, verbose_name='识别类别名称')),
                ('confidence', models.CharField(default='1', max_length=255, verbose_name='置信度')),
            ],
        ),
        migrations.CreateModel(
            name='DetectServer',
            fields=[
                ('detect_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('detect_name', models.CharField(blank=True, max_length=255, verbose_name='检测任务')),
                ('detect_url', models.CharField(max_length=255, verbose_name='检测url')),
            ],
        ),
        migrations.CreateModel(
            name='DetectType',
            fields=[
                ('detect_type', models.IntegerField(primary_key=True, serialize=False, verbose_name='检测类别')),
                ('detect_describe', models.CharField(max_length=255, verbose_name='检测描述')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('picture_name', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False, verbose_name='图片唯一名称')),
                ('path', models.CharField(max_length=255, verbose_name='图片路径')),
                ('task', models.PositiveIntegerField(verbose_name='任务类型')),
                ('recognition', models.PositiveIntegerField(null=True, verbose_name='认可度')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_min', models.CharField(max_length=255, verbose_name='坐标x最小值')),
                ('y_min', models.CharField(max_length=255, verbose_name='坐标y最小值')),
                ('x_max', models.CharField(max_length=255, verbose_name='坐标x最大值')),
                ('y_max', models.CharField(max_length=255, verbose_name='坐标y最大值')),
                ('confidence', models.CharField(max_length=255, verbose_name='图片准确率')),
                ('classno', models.IntegerField(verbose_name='识别类别')),
                ('name', models.CharField(max_length=255, verbose_name='识别类别名称')),
                ('update_time', models.DateField(auto_now=True, null=True, verbose_name='更新时间')),
                ('create_time', models.DateField(auto_now_add=True, null=True, verbose_name='上传时间')),
                ('picture_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eye.picture', verbose_name='图片唯一名称')),
            ],
        ),
    ]
