from django.urls import path
from . import views

urlpatterns = [
   path('', views.login_view, name='login'),  # Cambia la ruta de '' a 'login/'
   path('welcome/', views.welcome_view, name='welcome'),
   # La siguiente linea ayudara a redirigir al usuario al apartado de registrar persona
   path('registrar_persona_prototipo/', views.registrar_persona_prototipo, name='registrar_persona_prototipo'),
]
