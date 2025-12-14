from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.ver_carrinho, name='ver'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar'),
    path('remover/<int:produto_id>/', views.remover_do_carrinho, name='remover'),
    path('alterar/<int:produto_id>/<str:acao>/', views.alterar_quantidade, name='alterar'),
]
