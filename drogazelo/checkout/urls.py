from django.urls import path
from .views import finalizar_pedido
from .views import checkout

urlpatterns = [
    path('', checkout, name='checkout'),
    path('finalizar/', finalizar_pedido, name='finalizar_pedido'),
]
