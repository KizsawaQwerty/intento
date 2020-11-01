from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('templates/categorias', views.placasmadres, name="placasmadres"),
]

