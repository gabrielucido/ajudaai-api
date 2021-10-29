# pylint:disable=unused-argument
from rest_framework import permissions

class ActionPermissionMixin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if view.action == 'list':
            return self.list(request)
        if view.action == 'create':
            return self.create(request)
        self.extra_actions(self, request)
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if view.action == 'retrieve':
            return self.retrieve(request, obj)
        if view.action == 'update':
            return self.update(request, obj)
        if view.action == 'partial_update':
            return self.partial_update(request, obj)
        if view.action == 'destroy':
            return self.destroy(request, obj)
        self.extra_obj_actions(self, request, obj)
        return False

    def extra_actions(self, request):
        pass

    def extra_obj_actions(self, request, obj):
        pass

    def list(self, request):
        return True

    def create(self, request):
        return True

    def retrieve(self, request, obj):
        return False

    def update(self, request, obj):
        return False

    def partial_update(self, request, obj):
        return False

    def destroy(self, request, obj):
        return False
