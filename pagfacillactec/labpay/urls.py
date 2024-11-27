from django.urls import path

from pagfacillactec.labpay.migrations import views

urlpatterns = [
    path("", views.index, name="index"),
]