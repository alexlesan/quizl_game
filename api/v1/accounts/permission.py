from rest_framework import permissions


class IsGuest(permissions.BasePermission):
    """
    permission only for Guest users
    """
    message = 'Authenticated user is not allowed to access this page.'

    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)


class IsSuperUser(permissions.BasePermission):
    """
    permission to check if user has super user permissions
    """
    message = "You don't have enough permissions"

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsOwnerUser(permissions.BasePermission):
    """
    permission to check if logged user is the owner of data
    """
    message = "You can't access this page"

    def has_permission(self, request, view):
        user_id = request.GET.get('user_id')
        return bool(request.user and request.user.id == user_id)
