from rest_framework import permissions

class MyUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj==request.user