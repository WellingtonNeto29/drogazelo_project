# drogazelo/urls.py
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from . import views  # se suas views estiverem no mesmo app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_produtos, name='lista_produtos'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('adicionar/<int:produto_id>/', views.adicionar_produto, name='adicionar'),
    path('comprar/<int:produto_id>/', views.comprar_produto, name='comprar'),  # nova URL
]
