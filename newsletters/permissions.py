from rest_framework.permissions import BasePermission


class NewslettersPermissions(BasePermission):

    def has_permission(self, request, view):
        print(request.user.is_authenticated)
        print(request.method)
        print(request.user.is_staff)
        if request.method == 'POST' and not request.user.is_authenticated or request.user.is_staff:
            print('entra')
            return False
        print('no entra')
        return True