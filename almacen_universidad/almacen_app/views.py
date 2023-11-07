from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
#importamos la clase persona y un mensaje de alerta 
from .models import Persona #importamos la clase persona
from almacen_app.models import Persona
from django.contrib import messages
from .forms import RegistroPersonaForm #importación del formulario

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
        form = RegistroPersonaForm(request.POST) #ingresamos la forma del formulario que crearemos
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

            # Agrega un mensaje de éxito
            messages.success(request, '¡Registro exitoso!')

            return redirect('welcome')  # Reemplaza 'nombre_de_la_vista_registro' con el nombre de la vista de registro.

    else:
        form = RegistroPersonaForm()

    return render(request, 'registro_persona_prototipo.html', {'form': form})
# Fin de la clonación

@login_required(login_url='login')  # Esto asegura que solo usuarios autenticados puedan acceder a esta vista
def welcome_view(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    else:
    # Redirige al inicio si el usuario no esta registrado
    return render(request, 'login') 
