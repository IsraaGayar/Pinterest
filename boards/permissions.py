from rest_framework import permissions

class IsColaboratorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            print(obj.collaborator.all())
            return True
        return (obj.owner==request.user) or (request.user in obj.collaborator.all())

