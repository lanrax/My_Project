# regtoken/urls.py

from django.urls import path
# from .views import registration
from .views import UserCreateViewSet
from rest_framework.authtoken import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenObtainSlidingView,TokenRefreshSlidingView

urlpatterns = [
    path('register/', UserCreateViewSet.as_view({
        'post': 'create'}), name='register'),

    path('api-token-auth/', views.obtain_auth_token)
    # path("token/", TokenObtainSlidingView.as_view(), name="token_obtain_pair"),
    # path("refresh/", TokenRefreshSlidingView.as_view(), name="token_refresh"),
]
