from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.ver_carrinho, name='ver'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar'),
    path('comprar/<int:produto_id>/', views.comprar_agora, name='comprar'),
    path('remover/<int:produto_id>/', views.remover, name='remover'),
]
