from autoslug import AutoSlugField

from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseFields
from issues.models import Issue
from comments.models import Commentary


class Report(BaseFields):
    """
    Report Model.
    """
    user = models.ForeignKey(get_user_model(), verbose_name='Usuário', on_delete=models.CASCADE, related_name='received_reports', blank=True, null=True)
    commentary = models.ForeignKey(Commentary, verbose_name='Comentário', on_delete=models.CASCADE, related_name='reports', blank=True, null=True)
    issue = models.ForeignKey(Issue, verbose_name='Problema', on_delete=models.CASCADE, related_name='reports', blank=True, null=True)
    reported_by = models.ForeignKey(get_user_model(), verbose_name='Reportado Por', on_delete=models.CASCADE, related_name='created_reports', blank=False, null=False)
    description = models.CharField(verbose_name='Descrição', max_length=255, null=False, blank=False)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        """
        Model Options.
        """
        verbose_name = 'Denúncia'
        verbose_name_plural = 'Denúncias'
