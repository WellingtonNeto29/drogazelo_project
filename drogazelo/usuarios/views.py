from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})


def login_view(request):
    erro = False

    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            erro = True

    
    return render(request, 'usuarios/login.html', {'erro': erro})
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/login/')
