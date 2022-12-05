from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request):
    nombre = "German"
    return render(request, 
    "ejemplo/saludar_a.html",
    {"nombre":nombre})
