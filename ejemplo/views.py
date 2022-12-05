from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request):
    nombre = "German"
    return render(request, 
    "ejemplo/saludar_a.html",
    {"nombre":nombre})

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})