from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boleto/', views.gerar_boleto, name='gerar_boleto'),
]