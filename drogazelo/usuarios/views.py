from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Preencha todos os campos')
            return redirect('usuarios:cadastro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe')
            return redirect('usuarios:cadastro')

        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('usuarios:login')

    return render(request, 'usuarios/cadastro.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('lista_produtos')

        messages.error(request, 'Usuário ou senha inválidos')
        return redirect('usuarios:login')

    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('usuarios:login')
