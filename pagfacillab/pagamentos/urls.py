from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gerar_boleto/', views.gerar_boleto, name='gerar_boleto'),
    path('lista_documentos/', views.lista_documentos, name='lista_documentos'),
]