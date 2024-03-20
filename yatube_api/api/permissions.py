from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Разрешение на доступ к изменению объекта только для его создателя."""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
