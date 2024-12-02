from django.contrib import admin
from django.http import JsonResponse

from .models import Pagamento

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'cpf_cnpj', 'aprovado', 'data_solicitacao')
    list_filter = ('aprovado', 'data_solicitacao')
    actions = ['aprovar_pagamentos']

    # Ação personalizada para aprovar pagamentos no Admin
    def aprovar_pagamentos(self, request, queryset):
        queryset.update(aprovado=True)
        self.message_user(request, "Pagamentos aprovados com sucesso.")
    aprovar_pagamentos.short_description = "Aprovar pagamentos selecionados"


    def listar_pendentes(request):
        if not request.user.is_staff:
            return JsonResponse({'error': 'Permissão negada'}, status=403)

        pagamentos_pendentes = Pagamento.objects.filter(aprovado=False)
        data = [{'id': p.id, 'nome_cliente': p.nome_cliente, 'servico': p.servico} for p in pagamentos_pendentes]
        return JsonResponse({'pendentes': data})

