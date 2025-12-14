from django.contrib import admin
from django.urls import path, include
from produtos.views import lista_produtos

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicial
    path('', lista_produtos, name='lista_produtos'),

    # Apps com prefixo
    path('usuarios/', include('usuarios.urls')),
    path('carrinho/', include('carrinho.urls')),
    path('checkout/', include('checkout.urls')),
]
