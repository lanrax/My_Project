"""eyedetected URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('inddetect/', include('eyedetected.eye.urls')),
    # path('auth/', include('rest_framework.urls')),
    # # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # 新添加
    # # path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/regtoken/', include('regtoken.urls'), name='regtoken'),
    path('eye/', include("eyedetected.eye.urls")),


]
