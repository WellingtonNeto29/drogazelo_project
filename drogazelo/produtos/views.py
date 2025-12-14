from django.shortcuts import render
from .models import Produto
from django.shortcuts import render, redirect


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})
