from django.shortcuts import render

def home(request):
    return render (request, 'core/home.html')

def crear_cuenta(request):
    return render(request, 'core/crear cuenta.html') 

