from django.shortcuts import render, redirect
from django.http import HttpResponse   
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def login_view(request):
    erro = False

    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user:
            login(request, user)
            return redirect('lista_produtos')
        else:
            erro = True

    return render(request, 'usuarios/login.html', {'erro': erro})


def logout_view(request):
    logout(request)
    return redirect('login')


def cadastro(request):
    erro = False

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            erro = True
        else:
            User.objects.create_user(username=username, password=password)
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'erro': erro})


def comprar_produto(request, produto_id):
    # lógica para comprar o produto
    return HttpResponse(f"Produto {produto_id} comprado!")
