from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from produtos.models import Produto


@login_required
def adicionar_ao_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})

    produto_id = str(produto_id)
    carrinho[produto_id] = carrinho.get(produto_id, 0) + 1

    request.session['carrinho'] = carrinho
    request.session.modified = True

    return redirect('lista_produtos')


@login_required
def comprar_agora(request, produto_id):
    """
    Adiciona o produto ao carrinho e redireciona direto para o carrinho
    """
    carrinho = request.session.get('carrinho', {})

    produto_id = str(produto_id)
    carrinho[produto_id] = carrinho.get(produto_id, 0) + 1

    request.session['carrinho'] = carrinho
    request.session.modified = True

    return redirect('carrinho:ver')


@login_required
def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    itens = []
    total = 0

    for produto_id, quantidade in carrinho.items():
        produto = get_object_or_404(Produto, id=produto_id)
        subtotal = produto.preco * quantidade
        total += subtotal

        itens.append({
            'produto': produto,
            'quantidade': quantidade,
            'subtotal': subtotal
        })

    return render(request, 'carrinho/carrinho.html', {
        'itens': itens,
        'total': total
    })


@login_required
def remover(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    produto_id = str(produto_id)

    if produto_id in carrinho:
        del carrinho[produto_id]

    request.session['carrinho'] = carrinho
    request.session.modified = True

    return redirect('carrinho:ver')
