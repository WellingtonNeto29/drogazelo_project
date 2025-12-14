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
    return redirect('ver_carrinho')


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
def alterar_quantidade(request, produto_id, acao):
    carrinho = request.session.get('carrinho', {})
    produto_id = str(produto_id)

    if produto_id in carrinho:
        if acao == 'mais':
            carrinho[produto_id] += 1
        elif acao == 'menos' and carrinho[produto_id] > 1:
            carrinho[produto_id] -= 1

    request.session['carrinho'] = carrinho
    request.session.modified = True
    return redirect('ver_carrinho')


@login_required
def remover_do_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    produto_id = str(produto_id)

    if produto_id in carrinho:
        del carrinho[produto_id]

    request.session['carrinho'] = carrinho
    request.session.modified = True
    return redirect('ver_carrinho')
