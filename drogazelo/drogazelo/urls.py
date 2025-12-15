from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produtos.urls')),
    path('carrinho/', include('carrinho.urls')),
    path('checkout/', include('checkout.urls')),
    path('usuarios/', include('usuarios.urls')),
]
