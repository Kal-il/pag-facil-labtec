from django.db import models

class Pagamento(models.Model):
    nome_cliente = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    servico = models.TextField() #padrão: "modelagem e impressão 3d de objetos"
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)  # Para o administrador aprovar

