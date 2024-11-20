from rest_framework.viewsets import ModelViewSet
from apps.user.models import User
from apps.user.api.v1.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
