from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Custom permission to allow only the owner or a superuser to perform actions.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is the owner of the object or a superuser.
        """
        return obj == request.user
