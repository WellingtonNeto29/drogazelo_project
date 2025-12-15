from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(request, username=username, password=senha)

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return render(request, 'usuarios/login.html')


def cadastro_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe')
            return redirect('usuarios:cadastro')

        User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )

        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('usuarios:login')

    return render(request, 'usuarios/cadastro.html')


def logout_view(request):
    logout(request)
    return redirect('usuarios:login')