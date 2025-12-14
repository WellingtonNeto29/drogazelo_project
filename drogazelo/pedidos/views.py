from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from produtos.models import Produto
from .models import Pedido, ItemPedido

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = Produto.objects.get(id=produto_id)

    pedido, criado = Pedido.objects.get_or_create(
        usuario=request.user,
        finalizado=False
    )

    item, criado = ItemPedido.objects.get_or_create(
        pedido=pedido,
        produto=produto
    )

    if not criado:
        item.quantidade += 1
        item.save()

    return redirect('/')
