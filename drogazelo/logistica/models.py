from django.db import models
from django.contrib.auth.models import User
from checkout.models import Pedido

class Entregador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='entregador_perfil')
    telefone = models.CharField(max_length=20)
    placa_veiculo = models.CharField(max_length=10)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.placa_veiculo}"

class Entrega(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Rota', 'Em Rota'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado'),
    ]

    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='entrega')
    entregador = models.ForeignKey(Entregador, on_delete=models.SET_NULL, null=True, blank=True, related_name='entregas')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    endereco_entrega = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Entrega do Pedido #{self.pedido.id} - {self.status}"
