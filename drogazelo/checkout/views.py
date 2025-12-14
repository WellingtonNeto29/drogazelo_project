from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from checkout.models import Pedido
from produtos.models import Produto


@login_required
def finalizar_pedido(request):
    carrinho = request.session.get('carrinho', {})
    total = 0

    for produto_id, qtd in carrinho.items():
        produto = Produto.objects.get(id=produto_id)
        total += produto.preco * qtd

    if request.method == 'POST':
        Pedido.objects.create(
            usuario=request.user,
            endereco=request.POST['endereco'],
            telefone=request.POST['telefone'],
            metodo_pagamento=request.POST['metodo_pagamento'],
            total=total
        )

        del request.session['carrinho']
        return redirect('lista_produtos')

    return render(request, 'checkout/finalizar.html', {'total': total})
