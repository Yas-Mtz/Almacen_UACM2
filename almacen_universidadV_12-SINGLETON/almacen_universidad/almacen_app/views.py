from .models import Singleton  # Asegúrate de importar correctamente
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Persona  # importamos la clase persona
from .models import Rol  # importamos la clase persona
from almacen_app.models import Persona
from django.contrib import messages
from .forms import RegistroPersonaForm
from .models import Singleton  # SINGLETON


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirige a la página de bienvenida (puedes cambiar 'welcome' por la URL que prefieras).
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
            nueva_persona.contrasena = form.cleaned_data['contrasena']
            nueva_persona.id_rol = Rol.objects.get(
                nombre_rol=form.cleaned_data['id_rol'])

            # Guarda la nueva instancia en la base de datos
            nueva_persona.save()

            # Agrega un mensaje de éxito
            messages.success(request, '¡Registro exitoso!')

            # Reemplaza 'nombre_de_la_vista_registro' con el nombre de la vista de registro.
            return redirect('welcome')

    else:
        form = RegistroPersonaForm()

    return render(request, 'registro_persona_prototipo.html', {'form': form})
# Fin de la clonación


@login_required(login_url='login')
def welcome_view(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    else:
        # Redirige al inicio de sesión si el usuario no está autenticado
        return redirect('login')

# SINGLETON

# clase "LoginManager" heredea del singleton, en donde se encuantra el patron Singleton


class LoginManager(Singleton):
    # el método "__new__" se encarga de la creación de nuevas instancias
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # verificacion de instancias
            cls._instance = super(LoginManager, cls).__new__(
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
