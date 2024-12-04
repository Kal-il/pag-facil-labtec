from django.shortcuts import render
from django.http import HttpResponse
from .admin import CustomPagamentoForm
from docx import Document
from typing import Any

from .admin import CustomPagamentoForm


def home(request: Any) -> Any:
    return render(request, 'home.html')



def gerar_boleto(request: Any) -> Any:
    form = CustomPagamentoForm()
    if request.method == "POST":
        form = CustomPagamentoForm(request.POST)
        if form.is_valid():
            # Process the form data and generate the document
            nome_cliente = form.cleaned_data['nome_cliente']
            cpf_cnpj = form.cleaned_data['cpf_cnpj']
            endereco = form.cleaned_data['endereco']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            servico = form.cleaned_data['servico']

            # Generate the document
            doc = Document()
            doc.add_heading('Boleto de Pagamento', 0)
            doc.add_paragraph(f'Nome do Cliente: {nome_cliente}')
            doc.add_paragraph(f'CPF/CNPJ: {cpf_cnpj}')
            doc.add_paragraph(f'Endereço: {endereco}')
            doc.add_paragraph(f'Email: {email}')
            doc.add_paragraph(f'Telefone: {telefone}')
            doc.add_paragraph(f'Serviço: {servico}')

            # Save the document in a temporary file
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename="boleto_{nome_cliente}.docx"'
            doc.save(response)
            return response

    return render(request, "pagamentos.html", {"form": form})
# Create your views here.
