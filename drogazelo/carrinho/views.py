from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from produtos.models import Produto


@login_required
def adicionar_ao_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})

    carrinho[str(produto_id)] = carrinho.get(str(produto_id), 0) + 1

    request.session['carrinho'] = carrinho

    return redirect('lista_produtos')

from django.shortcuts import redirect

def comprar_agora(request, produto_id):
    # cria um carrinho novo só com esse produto
    request.session['carrinho'] = {str(produto_id): 1}
    return redirect('ver_carrinho')


@login_required
def comprar_agora(request, produto_id):
    carrinho = {}

    carrinho[str(produto_id)] = 1

    request.session['carrinho'] = carrinho

    return redirect('ver_carrinho')


@login_required
def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    produtos = []
    total = 0

    for produto_id, quantidade in carrinho.items():
        produto = get_object_or_404(Produto, id=produto_id)
        produto.quantidade = quantidade
        produto.subtotal = produto.preco * quantidade
        total += produto.subtotal
        produtos.append(produto)

    return render(request, 'carrinho/carrinho.html', {
        'produtos': produtos,
        'total': total
    })
    from django.shortcuts import redirect, get_object_or_404
from produtos.models import Produto

def adicionar_ao_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', [])

    produto = get_object_or_404(Produto, id=produto_id)
    carrinho.append(produto.id)

    request.session['carrinho'] = carrinho

    return redirect('lista_produtos')

