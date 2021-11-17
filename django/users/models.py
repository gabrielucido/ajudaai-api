from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    User Model.
    """

    def __str__(self):
        return self.username

    class Meta:
        """
        User Options.
        """
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
