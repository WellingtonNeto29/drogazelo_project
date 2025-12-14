from django.db import models
from django.contrib.auth.models import User

class Checkout(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    endereco = models.TextField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Checkout #{self.id}'
