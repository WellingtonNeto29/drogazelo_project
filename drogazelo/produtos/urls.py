from django.urls import path
from .views import lista_produtos

app_name = 'produtos'

urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),
]
