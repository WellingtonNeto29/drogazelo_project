from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
