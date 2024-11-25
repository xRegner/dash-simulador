from django.urls import path
from . import views

urlpatterns = [
    path('grafica/', views.grafica, name='grafica'),
]