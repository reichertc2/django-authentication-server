from rest_framework import permissions


class IsInspectorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if obj.inspector is None:
            return True

        return obj.inspector == request.user
            