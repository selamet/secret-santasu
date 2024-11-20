from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from apps.user.permissions import IsOwner
from apps.user.models import User
from apps.user.api.v1.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    ViewSet for managing User model.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Set permissions for different actions.
        """
        if self.action in ['create']:
            return [AllowAny()]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            return [IsAuthenticated(), IsOwner() or IsAdminUser()]

        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        """
        Overriding the default create method to include access and refresh tokens in the response.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Save the user

        # If UserSerializer.create() returns tokens, include them in the response
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        Overriding the default update method to handle custom logic.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Return the updated user data without tokens
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """
        Overriding the default partial update method to handle custom logic.
        """
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
