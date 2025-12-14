from django.urls import path
from .views import finalizar_pedido

urlpatterns = [
    path('finalizar/', finalizar_pedido, name='finalizar_pedido'),
]
