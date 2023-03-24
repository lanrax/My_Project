from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('detect_service', DetectURLGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('detect_service/update_server', DetectURLGenericViewSets.as_view({
        'post': 'update',
    })),
    path('detect_service/delete_server', DetectURLGenericViewSets.as_view({
        'post': 'delete',
    })),
    # 烟火检测
    path('fire_sync', FireDetectGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    re_path('^result/(?P<pid>\w{8}(-\w{4}){3}-\w{12})', FireDetectGenericViewSets.as_view({
        'get': 'retrieve',
    })),
    # 红外烟火检测
    path('fire_infrared_sync', FireInfraredDetectGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),

    # 入侵检测
    path('invasion_sync', InvasionDetectGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),

    # 红外入侵检测
    path('invasion_infrared_sync', InvasionInfraredDetectGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),

    # 人群密度检测
    path('crowd_sync', CrowdDetectGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),

    # 红外人群密度检测
    path('crowd_infrared_sync', CrowdInfraredDetectGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),

    # 图片质量评价
    path('recognize', RecognizeGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    }))
]
