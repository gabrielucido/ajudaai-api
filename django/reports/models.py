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
    comments = models.ManyToManyField(Comentary, verbose_name='Comentários', related_name='reports', blank=True)
    image = models.ImageField(upload_to='reports/%Y/%m/%d/', blank=True, null=True)

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
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'


class Vote(BaseFields):
    """
    Vote Model.
    """
    report = models.ForeignKey(Report, verbose_name='Ajudaai', on_delete=models.CASCADE, related_name='votes', blank=False, null=False)
    upvote = models.BooleanField(verbose_name='Upvote', blank=True, null=False, default=True)
    #token = models.CharField(verbose_name='token', blank=False, null=False)
    class Meta:
        """
        Model Options.
        """
        verbose_name = 'Voto'
        verbose_name_plural = 'Votos'
