from rest_framework import permissions

class OnlyStaffCanPost(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == "POST":
            if request.user.is_staff:
                return True
            else:
                return False
        
        return True