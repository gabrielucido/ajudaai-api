from rest_framework import exceptions

from django.core.exceptions import ValidationError


def prevent_not_found(pk, model, queryset):
    if pk:
        try:
            model.objects.get(pk=pk)
        except model.DoesNotExist as error:
            raise exceptions.NotFound from error
        except ValidationError as error:
            raise exceptions.ValidationError from error
        if not queryset.filter(pk=pk).exists():
            raise exceptions.PermissionDenied


def get_or_raise_error(pk, model):
    if pk:
        try:
            instance = model.objects.get(pk=pk)
        except model.DoesNotExist as error:
            raise exceptions.NotFound from error
        except ValidationError as error:
            raise exceptions.ValidationError from error
        return instance
    raise exceptions.ValidationError
