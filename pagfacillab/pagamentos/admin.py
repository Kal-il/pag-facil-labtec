from django.contrib import admin
from .models import Pagamento
from django import forms

# Register your models here.
class CustomPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['nome_cliente', 'cpf_cnpj', 'endereco', 'email', 'telefone', 'servico']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['readonly'] = True
