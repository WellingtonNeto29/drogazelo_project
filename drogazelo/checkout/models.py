from django.db import models
from django.contrib.auth.models import User


class Pedido(models.Model):
    METODOS_PAGAMENTO = [
        ('pix', 'Pix'),
        ('cartao', 'Cartão de crédito'),
        ('boleto', 'Boleto'),
        ('dinheiro', 'Dinheiro'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pedidos_checkout'
    )
    endereco = models.TextField()
    telefone = models.CharField(max_length=20)
    metodo_pagamento = models.CharField(max_length=20, choices=METODOS_PAGAMENTO)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"
