# pylint:disable=invalid-name,invalid-str-returned
import uuid

from django.db import models


class BaseFields(models.Model):
    """
    Base Fields Model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(
        verbose_name='Criado Em', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Atualizado Em', auto_now=True)

    class Meta:
        """
        Meta Class
        """
        abstract = True
