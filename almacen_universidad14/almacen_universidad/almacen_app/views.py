from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Persona, Rol
from django.contrib import messages
from .forms import RegistroPersonaForm
from django.shortcuts import render


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request, 'Error de autenticación. Verifica tu nombre de usuario y contraseña.')

    return render(request, 'login.html')

def registrar_persona_prototipo(request):
    if request.method == 'POST':
        form = RegistroPersonaForm(request.POST)
        if form.is_valid():
            prototipo = Persona.objects.first().clone()
            nueva_persona = prototipo.clone()

            nueva_persona.nombre = form.cleaned_data['nombre']
            nueva_persona.apellido_paterno = form.cleaned_data['apellido_paterno']
            nueva_persona.apellido_materno = form.cleaned_data['apellido_materno']
            nueva_persona.telefono = form.cleaned_data['telefono']
            nueva_persona.correo = form.cleaned_data['correo']
            nueva_persona.contrasena = form.cleaned_data['contrasena']
            nueva_persona.id_rol = Rol.objects.get(nombre_rol=form.cleaned_data['id_rol'])

            nueva_persona.save()

            messages.success(request, '¡Registro exitoso!')
            return redirect('welcome')

    else:
        form = RegistroPersonaForm()

    return render(request, 'registro_persona_prototipo.html', {'form': form})

def registrar_productos(request):
    # Lógica para registrar productos
    return render(request, 'registrar_productos.html')

def generar_reportes(request):
    # Lógica para generar reportes
    return render(request, 'generar_reportes.html')

def solicitar_almacen_central(request):
    # Lógica para solicitar productos al almacén central
    return render(request, 'solicitud_almacen_central.html')

def solicitar_productos(request):
    # Lógica para solicitar productos
    return render(request, 'solicitud_productos.html')


@login_required(login_url='login')
def welcome_view(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    else:
        return redirect('login')
