"""Ciclos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from TEM import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index"),
    path('Listado/', views.listado, name="Listado"),
    path('Limpieza/', views.limpieza, name="Limpieza"),
    path('Depirogenado/', views.depirogenado, name="Depirogenado"),
    path('Autoclave/', views.autoclave, name="Autoclave"),
    path('Estufa/', views.estufa, name="Estufa"),
    path('Uso/', views.uso, name="Uso"),
    path('Usuarios/', views.usuarios, name="Usuarios"),
]
