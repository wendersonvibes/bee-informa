from django.db import models
from django.contrib.auth.models import AbstractUser

# Tabela de usuários
class Usuario(AbstractUser):
    pass

    def __str__(self):
        return self.username
