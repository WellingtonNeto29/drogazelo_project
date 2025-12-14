from django.contrib import admin
from django.urls import path, include
from produtos.views import lista_produtos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_produtos, name='lista_produtos'),
    path('', include('usuarios.urls')),
    path('', include('carrinho.urls')),
]
