from django.urls import path, re_path
from .views_origin import *
from .views_base import FireDetectBaseGenericViewSets, FireInfraredBaseGenericViewSets, \
    InvasionBaseDetectGenericViewSets, InvasionInfraredBaseDetectGenericViewSets, CrowdBaseDetectGenericViewSets, \
    CrowdInfraredBaseDetectGenericViewSets
from django.views.static import serve
from eyedetected.settings import MEDIA_ROOT
from .views_strategy import FireDetectBaseStrategyGenericViewSets, FireInfraredBaseStrategyGenericViewSets
from eyedetected.eye import views

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

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

    re_path('^result/(?P<pid>\w{8}(-\w{4}){3}-\w{12})', FireDetectGenericViewSets.as_view({
        'get': 'retrieve',
    })),

    # 烟火检测
    path('fire_sync', FireDetectGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('fire_sync_base64', FireDetectBaseGenericViewSets.as_view({
        'post': 'create'
    })),
    re_path('^fire_sync_base64/(?P<pk>\d{1})', FireDetectBaseStrategyGenericViewSets.as_view({
        'post': 'create'
    })),

    # 红外烟火检测
    path('fire_infrared_sync', FireInfraredDetectGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('fire_infrared_sync_base64', FireInfraredBaseGenericViewSets.as_view({
        'post': 'create'
    })),
    re_path('^fire_infrared_sync_base64/(?P<pk>\d{1})', FireInfraredBaseStrategyGenericViewSets.as_view({
        'post': 'create'
    })),

    # 入侵检测
    path('invasion_sync', InvasionDetectGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('invasion_sync_base64', InvasionBaseDetectGenericViewSets.as_view({
        'post': 'create'
    })),

    # 红外入侵检测
    path('invasion_infrared_sync', InvasionInfraredDetectGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('invasion_infrared_sync_base64', InvasionInfraredBaseDetectGenericViewSets.as_view({
        'post': 'create'
    })),

    # 人群密度检测
    path('crowd_sync', CrowdDetectGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('crowd_sync_base64', CrowdBaseDetectGenericViewSets.as_view({
        'post': 'create'
    })),

    # 红外人群密度检测
    path('crowd_infrared_sync', CrowdInfraredDetectGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('crowd_infrared_sync_base64', CrowdInfraredBaseDetectGenericViewSets.as_view({
        'post': 'create'
    })),

    # 图片质量评价
    path('recognize', RecognizeGenericViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('fire_detect/', views.FireDetectView.as_view()),
    path('fire_infrared/', views.FireInfraredBaseGenericViewSets.as_view()),
    path('invasion_detect/', views.InvasionBaseDetectGenericViewSets.as_view()),
    path('invasion_infrared_detect/', views.InvasionInfraredBaseDetectGenericViewSets.as_view()),
    path('crowd_detect/', views.CrowdBaseDetectGenericViewSets.as_view()),
    path('crowd_infrared_detect/', views.CrowdInfraredBaseDetectGenericViewSets.as_view()),
]


