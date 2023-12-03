from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Persona, Rol, Singleton, Producto, ProductoFactory, Solicitud # Importamos el modelo persona, rol y SINGLETON
from .forms import RegistroPersonaForm # Formulario
from django.contrib.auth.hashers import make_password # Cifrado
from .forms import SolicitudForm
from .commands import SolicitudCommand

def login_view(request): #Logica para el registro de personas 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) # Verifica las credenciales de inicio
            return redirect('welcome') # Redirige a la página de bienvenida (welcome)
        else: 
            pass # Manejo de error de autentificación
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
            nueva_persona.id_rol = Rol.objects.get(nombre_rol=form.cleaned_data['id_rol'])
            
            # Guarda la nueva instancia en la base de datos
            nueva_persona.save()
            return redirect('welcome') # Si el registro es exitoso se envia a la pestaña de welcome  
    else:
        form = RegistroPersonaForm()

    return render(request, 'registro_persona_prototipo.html', {'form': form})
# Fin de la clonación

@login_required(login_url='login') # Protección para usuarios no registrados 
def welcome_view(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    else:
        return redirect('login') # Redirige al inicio de sesión si el usuario no está autenticado

##############
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
        id_producto = request.POST['id_producto']
        nombre = request.POST['nombre']
        cantidad = request.POST['cantidad']

        producto_factory = ProductoFactory()
        producto = producto_factory.create_producto(id_producto, nombre, cantidad)

        return redirect('lista_productos')  # Redirecciona a la página de lista de productos o a donde desees

    return render(request, 'registrar_productos.html')
