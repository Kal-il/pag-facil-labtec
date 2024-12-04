from django.contrib import admin
from .models import Pagamento
from django import forms

# Register your models here.
class CustomPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['nome_cliente', 'cpf_cnpj', 'inscricao_estadual', 'inscricao_municipal', 'endereco', 'cidade',
                  'estado', 'cep',  'email', 'telefone', 'servico']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inscricao_estadual'].required = False
        self.fields['inscricao_municipal'].required = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['readonly'] = True
