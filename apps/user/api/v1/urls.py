from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from apps.user.api.v1.views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
]
