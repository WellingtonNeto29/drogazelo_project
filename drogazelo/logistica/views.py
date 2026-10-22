from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Entrega, Entregador
from django.core.exceptions import ObjectDoesNotExist

@login_required
def painel_entregador(request):
    try:
        entregador = request.user.entregador_perfil
    except ObjectDoesNotExist:
        # Se não for entregador, redireciona para a home
        return redirect('/')

    # Entregas que estão pendentes (sem entregador ou aguardando aceite)
    entregas_pendentes = Entrega.objects.filter(status='Pendente', entregador__isnull=True)

    # Entregas atuais do entregador
    minhas_entregas = Entrega.objects.filter(entregador=entregador).exclude(status='Entregue').exclude(status='Cancelado')

    return render(request, 'logistica/painel.html', {
        'entregador': entregador,
        'entregas_pendentes': entregas_pendentes,
        'minhas_entregas': minhas_entregas
    })

@login_required
def aceitar_entrega(request, entrega_id):
    try:
        entregador = request.user.entregador_perfil
    except ObjectDoesNotExist:
        return redirect('/')

    entrega = get_object_or_404(Entrega, id=entrega_id, status='Pendente', entregador__isnull=True)

    entrega.entregador = entregador
    entrega.status = 'Em Rota'
    entrega.save()

    return redirect('logistica:painel')

@login_required
def atualizar_status_entrega(request, entrega_id):
    try:
        entregador = request.user.entregador_perfil
    except ObjectDoesNotExist:
        return redirect('/')

    entrega = get_object_or_404(Entrega, id=entrega_id, entregador=entregador)

    novo_status = request.POST.get('status')
    if novo_status in [choice[0] for choice in Entrega.STATUS_CHOICES]:
        entrega.status = novo_status
        entrega.save()

    return redirect('logistica:painel')
