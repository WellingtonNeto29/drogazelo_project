from django.shortcuts import redirect, get_object_or_404
from produtos.models import Produto
from django.shortcuts import render


def adicionar_ao_carrinho(request, produto_id):
    from django.shortcuts import redirect, get_object_or_404
from produtos.models import Produto

def comprar_agora(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    carrinho = request.session.get('carrinho', {})

    if str(produto_id) in carrinho:
        carrinho[str(produto_id)] += 1
    else:
        carrinho[str(produto_id)] = 1

    request.session['carrinho'] = carrinho

    # Redireciona direto para o carrinho (ou checkout depois)
    return redirect('ver_carrinho')

    produto = get_object_or_404(Produto, id=produto_id)

    carrinho = request.session.get('carrinho', {})

    if str(produto_id) in carrinho:
        carrinho[str(produto_id)] += 1
    else:
        carrinho[str(produto_id)] = 1

    request.session['carrinho'] = carrinho

    return redirect('lista_produtos')
def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    return render(request, 'carrinho/ver_carrinho.html', {'carrinho': carrinho})

