from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from apps.users.views import UserAPIViewSet


router = DefaultRouter()
router.register('user', UserAPIViewSet, 'api_users')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="api_user_login"),
    path('refresh/', TokenRefreshView.as_view(), name="api_user_refresh"),
]

urlpatterns += router.urls