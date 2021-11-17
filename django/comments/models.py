from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseFields


class Commentary(BaseFields):
    """
    Commentary Model.
    """
    user = models.ForeignKey(get_user_model(), verbose_name='Usuário', on_delete=models.CASCADE, related_name='comments', blank=False, null=False)
    text = models.CharField(verbose_name='Descrição', max_length=512, null=True, blank=False)
    visible = models.BooleanField(verbose_name='Visível', blank=True, null=False, default=True)

    class Meta:
        """
        Model Options.
        """
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
