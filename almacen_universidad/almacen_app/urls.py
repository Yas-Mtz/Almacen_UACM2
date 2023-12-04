from django.urls import path
from . import views

urlpatterns = [
   path('', views.login_view, name='login'), # Redirige la raíz a la vista de inicio de sesión
   path('welcome/', views.welcome_view, name='welcome'), # Redirige a la pagina del menú
   path('registrar_persona_prototipo/', views.registrar_persona_prototipo, name='registrar_persona_prototipo'),  # La siguiente linea ayudara a redirigir al usuario al apartado de registrar persona
   path('solicitud_exitosa/', views.solicitud_exitosa_view, name='solicitud_exitosa'),
   path('registrar_productos/', views.registrar_productos, name='registrar_productos'),
]
