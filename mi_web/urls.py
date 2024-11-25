"""
URL configuration for mi_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inicio.views import inicio, contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),  # Ruta para la página de inicio
    path('contacto/', contacto, name='contacto'), 
    path('', include('inicio.urls')),    
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]

