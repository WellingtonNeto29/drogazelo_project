from django.urls import path
from . import views

app_name = 'logistica'

urlpatterns = [
    path('painel/', views.painel_entregador, name='painel'),
    path('aceitar/<int:entrega_id>/', views.aceitar_entrega, name='aceitar'),
    path('atualizar/<int:entrega_id>/', views.atualizar_status_entrega, name='atualizar'),
]
