from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
#importamos la clase persona y un mensaje de alerta 
from .models import Persona #importamos la clase persona
from almacen_app.models import Persona
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirige a la página de bienvenida.
            return redirect('welcome')
        else:
            # Handle authentication error if needed
            pass

    return render(request, 'login.html')

# definimos la función del clonado para crear nuevas instancias 
def registrar_persona_prototipo(request):
    if request.method == 'POST':
         # Clona una instancia de Persona para usarla como prototipo
        prototipo = Persona.objects.first().clone()
        #creamos una instancia basada en el prototipo clonado 
        nueva_persona = prototipo.clone()
        # Completa los detalles con los datos del formulario
        nueva_persona.nombre = request.POST['Máximo Eduardo']
        nueva_persona.apellido_paterno = request.POST['Sánchez']
        nueva_persona.apellido_materno = request.POST['Gutiérrez']
        nueva_persona.telefono = request.POST['3948576238']
        nueva_persona.correo = request.POST['maximo.sanchez@uacm.edu.mx']
        nueva_persona.contrasena = request.POST['maximopower']
        # Guarda la nueva instancia en la base de datos
        nueva_persona.save()
# Agregamos un mensaje de exito al guardar un nuevo usuario (persona).
        messages.success(request, '¡Registro exitoso!')
# Y nos quedamos en la misma página de registro
        return redirect('nombre_de_la_vista_registro') 
return render(request, 'registro_persona_prototipo.html')
# Finalizamos la clonación.

@login_required(login_url='login')  # Esto asegura que solo usuarios autenticados puedan acceder a esta vista
def welcome_view(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    else:
    # Redirige al inicio si el usuario no esta registrado
    return render(request, 'login') 
