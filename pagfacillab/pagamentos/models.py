from django.db import models


class DocumentoBoleto(models.Model):
    nome_cliente = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='solicitacoes/')  # Salva na pasta 'boletos/'

    def __str__(self):
        return self.nome_cliente

class Pagamento(models.Model):
    nome_cliente = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=20)
    inscricao_estadual = models.CharField(max_length=20, blank=True, null=True)
    inscricao_municipal = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, null=True)
    cidade = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=20, null=True)
    cep = models.CharField(max_length=10, null=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    servico = models.TextField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)  # Para o administrador aprovar
