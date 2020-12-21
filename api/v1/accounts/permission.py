from rest_framework import permissions

class IsGuest(permissions.BasePermission):
    """
    permission only for Guest users
    """
    message = 'Authenticated user is not allowed to access this page.'

    def has_permission(self, request, view):
        return not request.user.is_authenticated
