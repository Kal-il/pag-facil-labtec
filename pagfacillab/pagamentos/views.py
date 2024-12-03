from django.shortcuts import render
from typing import Any


def home(request: Any) -> Any:
    return render(request, 'pagamentos.html')

def gerar_boleto(request: Any) -> Any:
    pass

# Create your views here.
