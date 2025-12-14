from django.urls import path
from .views import adicionar_ao_carrinho, comprar_agora, ver_carrinho

urlpatterns = [
    path('adicionar/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('comprar/<int:produto_id>/', comprar_agora, name='comprar_agora'),
    path('', ver_carrinho, name='ver_carrinho'),
]
