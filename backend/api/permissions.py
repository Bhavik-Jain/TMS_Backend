from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, obj):
        if obj.user:
            return request.user == obj.user
        else:
            return False