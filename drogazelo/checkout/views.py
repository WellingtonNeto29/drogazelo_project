from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def finalizar_pedido(request):
    if request.method == 'POST':
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        metodo = request.POST.get('metodo_pagamento')

        if not endereco or not telefone or not metodo:
            messages.error(request, 'Preencha todos os campos.')
            return redirect('checkout')

        # Limpa carrinho
        request.session['carrinho'] = {}

        messages.success(
            request,
            'Pedido confirmado! 🚚 Previsão de entrega: 1 a 2 horas.'
        )

        return redirect('lista_produtos')

    return render(request, 'checkout/finalizar.html')
