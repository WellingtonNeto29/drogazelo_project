from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from produtos.models import Produto
from checkout.models import Pedido
from logistica.models import Entrega
from django.db import transaction

@login_required
def checkout_view(request):
    carrinho = request.session.get('carrinho', {})
    itens = []
    total = 0

    for produto_id, quantidade in carrinho.items():
        produto = Produto.objects.get(id=produto_id)
        subtotal = produto.preco * quantidade
        total += subtotal

        itens.append({
            'produto': produto,
            'quantidade': quantidade,
            'subtotal': subtotal
        })

    if request.method == 'POST':
        # Dados do formulário
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        pagamento = request.POST.get('pagamento')

        with transaction.atomic():
            # Criar o Pedido
            pedido = Pedido.objects.create(
                usuario=request.user,
                endereco=endereco,
                telefone=telefone,
                metodo_pagamento=pagamento,
                total=total
            )

            # Criar a Entrega para o entregador
            Entrega.objects.create(
                pedido=pedido,
                endereco_entrega=endereco,
                status='Pendente'
            )

        # Limpa carrinho
        request.session['carrinho'] = {}
        request.session.modified = True

        return render(request, 'checkout/sucesso.html', {
            'nome': nome
        })

    return render(request, 'checkout/checkout.html', {
        'itens': itens,
        'total': total
    })
