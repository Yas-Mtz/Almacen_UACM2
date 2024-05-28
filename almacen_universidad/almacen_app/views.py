from multiprocessing import connection
from typing import Any
from django.http import (
    HttpResponseRedirect,
    HttpResponsePermanentRedirect,
    HttpResponse,
    JsonResponse
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from almacen_app.models import Persona as AlmacenPersona  # Importamos el modelo Persona desde la app almacen_app
from .models import Persona, Rol, Singleton, Producto, ProductoFactory, Solicitud
from .forms import RegistroPersonaForm, SolicitudForm, SolicitudAlmacenCentralForm
from .commands import SolicitudCommand
from django.shortcuts import render, redirect
from .models import Producto


# Resto del código


# Resto del código

def login_view(request): #logica para el registro de personas
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) # Verifica las credenciales de inicio
            # Redirige a la página de bienvenida
            return redirect('welcome')
        else:
            # Handle authentication error if needed
            pass
    return render(request, 'login.html')

# definimos la función que utilizara el clonado para crear una nueva instancia
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
            nueva_persona.contrasena = make_password(form.cleaned_data['contrasena'])
            nueva_persona.id_rol = Rol.objects.get(nombre_rol=form.cleaned_data['id_rol'])

            # Guarda la nueva instancia en la base de datos
            nueva_persona.save()
            #si el registro es exitoso se envia a la pestaña inicial
            return redirect('welcome')

    else:
        form = RegistroPersonaForm()

    return render(request, 'registro_persona_prototipo.html', {'form': form})
# Fin de la clonación

@login_required(login_url='login') # Protección para usuarios no registrados

def welcome_view(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    else:
        return redirect('login')  # Redirige al inicio de sesión si el usuario no está autenticado
    
#
def solicitud_producto_view(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)

            # Asignar el comando a la solicitud
            solicitud_command = SolicitudCommand(solicitud)
            solicitud.set_command(solicitud_command)

            # Procesar la solicitud
            solicitud.procesar_solicitud()

            # Puedes redirigir a la página de éxito o a donde consideres necesario
            return redirect('solicitud_exitosa')
    else:
        form = SolicitudForm()

    return render(request, 'solicitud_producto.html', {'form': form})

def solicitud_exitosa_view(request):
    return render(request, 'solicitud_exitosa.html')
##############

    # SINGLETON

# clase "LoginManager" heredea del singleton, en donde se encuantra el patron Singleton


class LoginManager(Singleton):
     logged_in_users = set()
    # el método "_new_" se encarga de la creación de nuevas instancias
def _new_(cls, *args, **kwargs):
        if cls._instance is None:  # verificacion de instancias
            cls.instance = super(LoginManager, cls).new_(
                cls)  # si no hay instancia se crea una
            # inicializa un conjunto para almacenar los usuarios que han iniciado sesión
            cls._instance.logged_in_users = set()
        # devuelve la única instancia de la clase, asegurandose que es unica instancia
        return cls._instance

    # metodo para iniciar sesión de un usuario
def login_user(self, request, username, password):
        # se usa la función "authenticate" para verificar las credenciales del usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:  # si la autenticación es exitosa:
            login(request, user)  # inicia sesión
            # agrega el nombre de usuario a la lista de usuarios conectados
            self.logged_in_users.add(username)
            return True  # "true" si el inicio de sesión fue exitoso
        return False  # "false" si no fue exitoso

    # metodo para obtener la lista de usuarios conectados
def get_logged_in_users(self):
        return self.logged_in_users  # devuelve el conjunto de usuarios conectados
    
#Apartado de metodo FactoryMethod

def registrar_productos(request):
    if request.method == 'POST':
        id_producto = request.POST.get('id_producto')
        nombre = request.POST.get('nombre_producto')
        cantidad = request.POST.get('cantidad')

        # Validar que los campos no estén vacíos
        if id_producto and nombre and cantidad:
            # Crear un nuevo objeto Producto y guardarlo en la base de datos
            producto = Producto.objects.create(id_producto=id_producto, nombre_producto=nombre, cantidad=cantidad)

            # Redireccionar a la página de lista de productos (ajusta la ruta según tu proyecto)
            return redirect('lista_productos')
        else:
            # Manejar el caso donde los campos no están completos
            error_message = 'Por favor, complete todos los campos del formulario.'
            return render(request, 'registrar_productos.html', {'error_message': error_message})

    return render(request, 'registrar_productos.html')



def generar_reportes_view(request: Any) -> HttpResponse:
    # Lógica para generar reportes
    return render(request, 'generar_reportes.html')

#Logica para enviar correos 
def solicitud_almacen_central_view(request: Any) -> (HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse):
    if request.method == 'POST':
        form = SolicitudAlmacenCentralForm(request.POST)
        if form.is_valid():
            # Guardar datos en la base de datos u otras operaciones necesarias

            # Enviar correo electrónico
            subject = 'Nueva Solicitud Registrada'
            message = f'Nueva solicitud registrada:\n\n{form.cleaned_data}'
            from_email = 'tucorreo@gmail.com'  # Reemplaza con tu dirección de correo
            recipient_list = ['destinatario@gmail.com']  # Reemplaza con la dirección del destinatario
            send_mail(subject, message, from_email, recipient_list)

            return redirect('pagina_de_exito')  # Reemplaza con la página de éxito deseada      
    else:
        form = SolicitudAlmacenCentralForm()

    return render(request, 'solicitud_almacen_central.html', {'form': form})

def obtener_datos_inventario(request):
    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        with connection.cursor() as cursor:
            cursor.callproc('ObtenerDatosInventario', [fecha_inicio, fecha_fin])
            results = cursor.fetchall()

        data = [{'nombre_producto': row[0], 'cantidad': row[1]} for row in results]
        return JsonResponse({'data': data})

    return JsonResponse({'error': 'Método no permitido'}, status=405)