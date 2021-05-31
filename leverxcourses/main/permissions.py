from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission

User = get_user_model()


class LecturerOrGetPermissions(BasePermission):
    allowed_user_roles = [User.LECTURER]

    def has_permission(self, request, view):
        is_allowed_user = request.user.role in self.allowed_user_roles
        return is_allowed_user or request.method == 'GET'
