from django.contrib.auth.models import AbstractUser
from django.db import models  # pylint: disable=unused-import


class User(AbstractUser):
    """
    User Model.
    """

    def __str__(self):
        return str(self.username)

    class Meta:
        """
        User Options.
        """
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
