from django.db import models

from core.models import BaseFields


class Animal(BaseFields):
    """
    Animal Model.
    """
    name = models.CharField(verbose_name='Nome', max_length=128, null=False, blank=False)
    description = models.CharField(verbose_name='Descrição', max_length=255, null=True, blank=False)

    def __str__(self):
      return self.name

    class Meta:
        """
        Model Options.
        """
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
