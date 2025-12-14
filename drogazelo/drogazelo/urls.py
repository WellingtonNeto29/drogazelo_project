from django.contrib import admin
from django.urls import path
from usuarios.views import cadastro, login_view, logout_view
from produtos.views import lista_produtos
from carrinho.views import adicionar_ao_carrinho



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login_view, name='login'),
    path('', lista_produtos, name='lista_produtos'),
    path('logout/', logout_view, name='logout'),
    path('adicionar/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar'),

]
