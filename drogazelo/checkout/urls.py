from django.urls import path
from .views import finalizar_pedido

urlpatterns = [
    path('', finalizar_pedido, name='checkout'),
]
