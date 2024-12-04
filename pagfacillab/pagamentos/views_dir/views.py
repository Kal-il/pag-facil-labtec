from django.shortcuts import render, redirect
from typing import Any
from ..models import DocumentoBoleto
import requests


def home(request: Any) -> Any:
    return render(request, 'home.html')


def gerar_boleto_view(request):
    if request.method == 'POST':
        dados = {
            'nome_cliente': request.POST['nome_cliente'],
            'cpf_cnpj': request.POST['cpf_cnpj'],
            'inscricao_estadual': request.POST.get('inscricao_estadual', ''),
            'inscricao_municipal': request.POST.get('inscricao_municipal', ''),
            'endereco': request.POST['endereco'],
            'cidade': request.POST['cidade'],
            'estado': request.POST['estado'],
            'cep': request.POST['cep'],
            'email': request.POST['email'],
            'telefone': request.POST['telefone'],
            'servico': request.POST['servico'],
        }
        # Armazena os dados na sessão para uso posterior
        request.session['dados_boleto'] = dados
        return render(request, 'confirmacao_boleto.html', {'dados': dados})  # Renderiza a página de confirmação

    return render(request, 'pagamentos.html')  # Página inicial do formulário


def confirmar_boleto(request):
    if request.method == 'POST':
        # Recupera os dados da sessão
        dados = request.session.get('dados_boleto')

        # Verifica se há dados na sessão
        if not dados:
            return redirect('gerar_boleto_view')  # Redireciona se não houver dados

        # Faz a requisição à API para gerar o documento
        response = requests.post('http://localhost:8000/pagamentos/api/gerar-boleto/', json=dados)

        if response.status_code == 200:
            # Obtém a URL do arquivo gerado
            file_url = response.json().get('file_url')
            return redirect(file_url)  # Redireciona para download

    return redirect('api/gerar-boleto')


def lista_documentos(request):
    documentos = DocumentoBoleto.objects.all()
    return render(request, 'lista_documentos.html', {'documentos': documentos})

