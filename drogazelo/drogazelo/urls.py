from django.contrib import admin
from django.urls import path
from usuarios.views import cadastro
from produtos.views import lista_produtos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', cadastro, name='cadastro'),
    path('', lista_produtos, name='lista_produtos'),
]
