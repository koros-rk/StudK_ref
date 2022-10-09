from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
