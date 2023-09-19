from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def GestionDeUsuarios(request):             # Crear funcion
    return render(request, 'Gestion/index.html')  # muestra index.html

def vista2(request):             # Crear funcion
    return render(request, 'Gestion/index2.html')  # muestra index.html



