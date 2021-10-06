from rest_framework.permissions import BasePermission


class NewslettersPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST' and not request.user.is_authenticated and not request.user.is_staff:
            return False
        return True