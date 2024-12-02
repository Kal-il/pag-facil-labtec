from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('pagamentos/', views.criar_pagamento, name='criar_pagamento'),
    path('pagamentos/aprovar/<int:pagamento_id>/', views.aprovar_pagamento, name='aprovar_pagamento'),
    # Adicione outras rotas aqui (ex.: visualizar, aprovar, gerar documento)
]
