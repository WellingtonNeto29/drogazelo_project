from django.urls import path
from .views import (
    adicionar_ao_carrinho,
    remover_do_carrinho,
    alterar_quantidade,
    ver_carrinho
)

urlpatterns = [
    path('carrinho/', ver_carrinho, name='ver_carrinho'),
    path('adicionar/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar'),
    path('remover/<int:produto_id>/', remover_do_carrinho, name='remover'),
    path('alterar/<int:produto_id>/<str:acao>/', alterar_quantidade, name='alterar'),
]
