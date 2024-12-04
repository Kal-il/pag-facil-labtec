from django.contrib import admin
from .models import DocumentoBoleto
from django import forms

# Register your models here.

@admin.register(DocumentoBoleto)
class DocumentoBoletoAdmin(admin.ModelAdmin):
    list_display = ['nome_cliente', 'data_criacao', 'arquivo']  # Campos exibidos na lista

