from django.contrib import admin
from django.urls import path
from . import views

# Lista de endpoints/urls definida en un path,recibe como parametro el nombre de la url 
# y lo que va a hacer
urlpatterns = [
    path('index/', views.index,name="index"),
    path('obtenerpost/', views.IndexView.as_view(),name="obtenerpost"),
]

