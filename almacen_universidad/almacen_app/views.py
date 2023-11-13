from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Persona #importamos la clase persona
from .forms import RegistroPersonaForm

def login_view(request): #Manejo del inicio de sesión
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirige a la página de bienvenida
            return redirect('welcome')
        else:
            # Manejo de error de autentificación 
            pass

    return render(request, 'login.html')

#Definimos la función que utilizara para el clonado para crear una nueva instancia (basada en un prototipo)
def registrar_persona_prototipo(request):
    if request.method == 'POST':
        form = RegistroPersonaForm(request.POST)
        if form.is_valid():
            # Crea una nueva instancia de Persona basada en el prototipo clonado
            prototipo = Persona.objects.first().clone()
            nueva_persona = prototipo.clone()

            # Completa los detalles con los datos del formulario
            nueva_persona.nombre = form.cleaned_data['nombre']
            nueva_persona.apellido_paterno = form.cleaned_data['apellido_paterno']
            nueva_persona.apellido_materno = form.cleaned_data['apellido_materno']
            nueva_persona.telefono = form.cleaned_data['telefono']
            nueva_persona.correo = form.cleaned_data['correo']
            nueva_persona.contrasena = form.cleaned_data['contrasena']

            # Guarda la nueva instancia en la base de datos
            nueva_persona.save()

            return redirect('welcome')  
            #Redirecciona al registrar no redirigue a la pestaña de inicio
    else:
        form = RegistroPersonaForm()

    return render(request, 'registro_persona_prototipo.html', {'form': form})
# Fin de la clonación

@login_required(login_url='login') #vista de bienvenida 
def welcome_view(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    else:
        return redirect('login')  
    # Redirige al inicio de sesión si el usuario no está autenticado
