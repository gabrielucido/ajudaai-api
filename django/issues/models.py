from autoslug import AutoSlugField

from django.db import models

from core.models import BaseFields


class Issue(BaseFields):
    """
    Issue Model.
    """
    title = models.CharField(verbose_name='Nome', max_length=128, null=False, blank=False)
    description = models.CharField(verbose_name='Descrição', max_length=255, null=True, blank=False)
    image = models.ImageField(upload_to='reports/%Y/%m/%d/', blank=True, null=True)
    visible = models.BooleanField(verbose_name='Visível', blank=True, null=False, default=True)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=False)

    def __str__(self):
      return self.title

    def get_upvotes(self):
        return self.votes.filter(upvote=True).count()

    def get_downvotes(self):
        return self.votes.filter(upvote=False).count()

    class Meta:
        """
        Model Options.
        """
        verbose_name = 'Problema'
        verbose_name_plural = 'Problemas'


class Vote(BaseFields):
    """
    Vote Model.
    """
    issue = models.ForeignKey(Issue, verbose_name='Problema', on_delete=models.CASCADE, related_name='votes', blank=False, null=False)
    upvote = models.BooleanField(verbose_name='Upvote', blank=True, null=False, default=True)
    token = models.CharField(verbose_name='token', max_length=64, blank=False, null=False)

    class Meta:
        """
        Model Options.
        """
        verbose_name = 'Voto'
        verbose_name_plural = 'Votos'
