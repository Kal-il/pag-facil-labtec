from django.urls import path, include
from .views_dir import views, views_api
from rest_framework.routers import DefaultRouter
from .views_dir.views_api import DocumentoBoletoViewSet


router = DefaultRouter()
router.register(r'api/boletos', DocumentoBoletoViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('gerar_boleto/', views.gerar_boleto_view, name='gerar_boleto'),
    path('lista_documentos/', views.lista_documentos, name='lista_documentos'),
    path('api/gerar-boleto/', views_api.gerar_boleto_api, name='gerar_boleto_api'),
    path('confirmar-boleto/', views.confirmar_boleto, name='confirmar_boleto'),
    path('', include(router.urls)),
]

path('', views.home, name='home'),
path('gerar_boleto/', views.gerar_boleto_view, name='gerar_boleto'),
path('lista_documentos/', views.lista_documentos, name='lista_documentos'),
path('confirmar-boleto/', views.confirmar_boleto, name='confirmar_boleto'),
path('', include(router.urls)),