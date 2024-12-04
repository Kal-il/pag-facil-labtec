from rest_framework import serializers
from .models import DocumentoBoleto

class DocumentoBoletoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoBoleto
        fields = '__all__'