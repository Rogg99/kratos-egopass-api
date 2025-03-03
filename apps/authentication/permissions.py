from rest_framework.permissions import BasePermission

class IsSystemAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.is_system_admin:
            return True 

        return False


"""
Implement permission using has perm attribute passing permission parameters

## @permission_classes([CustomPermission('app.model_permission')])
## permission_classes = [CustomPermission('app.model_permission')]
"""
class CustomPermission(BasePermission):
    def __init__(self, permission_name):
        self.permission_name = permission_name
    def has_permission(self, request, view):
        # Check if the user has the specified permission
        return request.user.has_perm(self.permission_name)
    def __call__(self, *args, **kwargs):
        return self
