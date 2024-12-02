from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from .models import Pagamento
from typing import Any
import json


def home(request: Any) -> Any:
    return render(request, 'pagamentos.html')

# Endpoint para criar uma nova solicitação de pagamento
def criar_pagamento(request):
    if request.method == 'POST':
        # Supondo que os dados venham no formato JSON
        data = json.loads(request.body)
        pagamento = Pagamento.objects.create(
            nome_cliente=data['nome_cliente'],
            cpf_cnpj=data['cpf_cnpj'],
            endereco=data['endereco'],
            email=data['email'],
            telefone=data['telefone'],
            servico=data['servico']
        )
        return JsonResponse({'message': 'Solicitação criada com sucesso!'}, status=201)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)


# View para aprovar uma solicitação de pagamento
def aprovar_pagamento(request, pagamento_id):
    if request.method == 'POST':
        # Verifique se o usuário é administrador (opcional, mas recomendado)
        if not request.user.is_staff:
            return JsonResponse({'error': 'Permissão negada'}, status=403)

        # Busca o pagamento específico
        pagamento = get_object_or_404(Pagamento, id=pagamento_id)

        # Aprova o pagamento
        pagamento.aprovado = True
        pagamento.save()

        return JsonResponse({'message': 'Pagamento aprovado com sucesso!'})
