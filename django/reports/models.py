from django.db import models

from core.models import BaseFields


class Comentary(BaseFields):
    text = models.CharField(verbose_name='Descrição', max_length=512, null=True, blank=False)


class Report(BaseFields):
    """
    Report Model.
    """
    title = models.CharField(verbose_name='Nome', max_length=128, null=False, blank=False)
    description = models.CharField(verbose_name='Descrição', max_length=255, null=True, blank=False)
    comments = models.ManyToManyField(Comentary, verbose_name='Comentários', related_name='reports', null=True)
    relevance = models.IntegerField(verbose_name='Ajudometro', blank=True, null=False, default=0)
    #image =

    def __str__(self):
      return self.name

    class Meta:
        """
        Model Options.
        """
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
