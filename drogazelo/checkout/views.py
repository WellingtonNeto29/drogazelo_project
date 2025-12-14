from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Checkout
from produtos.models import Produto

@login_required
def finalizar_pedido(request):
    carrinho = request.session.get('carrinho', {})
    total = 0

    for produto_id, quantidade in carrinho.items():
        produto = Produto.objects.get(id=produto_id)
        total += produto.preco * quantidade

    if request.method == 'POST':
        endereco = request.POST.get('endereco')

        Checkout.objects.create(
            usuario=request.user,
            endereco=endereco,
            total=total
        )

        request.session['carrinho'] = {}
        return redirect('lista_produtos')

    return render(request, 'pedidos/finalizar.html', {'total': total})
