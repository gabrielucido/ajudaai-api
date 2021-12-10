from rest_framework import exceptions

from django.core.exceptions import ValidationError


def prevent_not_found(p_k, model, queryset):
    if p_k:
        try:
            model.objects.get(p_k=p_k)
        except model.DoesNotExist as error:
            raise exceptions.NotFound from error
        except ValidationError as error:
            raise exceptions.ValidationError from error
        if not queryset.filter(p_k=p_k).exists():
            raise exceptions.PermissionDenied


def get_or_raise_error(p_k, model):
    if p_k:
        try:
            instance = model.objects.get(p_k=p_k)
        except model.DoesNotExist as error:
            raise exceptions.NotFound from error
        except ValidationError as error:
            raise exceptions.ValidationError from error
        return instance
    raise exceptions.ValidationError
