from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def listado(request):
    return render(request, "Listado.html")

def limpieza(request):
    return render(request, "Limpieza.html")

def depirogenado(request):
    return render(request, "Depirogenado.html")

def autoclave(request):
    return render(request, "Autoclave.html")

def estufa(request):
    return render(request, "Estufa.html")

def uso(request):
    return render(request, "Uso.html")

def usuarios(request):
    return render(request, "Usuarios.html")

# Create your views here.
