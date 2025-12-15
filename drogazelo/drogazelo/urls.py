from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicial / produtos
    path('', include('produtos.urls')),

    # Usuários
    path('usuarios/', include('usuarios.urls')),

    # Carrinho
    path('carrinho/', include('carrinho.urls')),

    # Checkout
    path('checkout/', include('checkout.urls')),
]
