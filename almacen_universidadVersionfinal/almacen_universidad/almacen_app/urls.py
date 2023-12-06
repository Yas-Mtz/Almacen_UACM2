from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Redirige la raíz a la vista de inicio de sesión
    path('welcome/', views.welcome_view, name='welcome'),
    path('registrar_persona_prototipo/', views.registrar_persona_prototipo, name='registrar_persona_prototipo'),
    path('welcome/solicitud_producto/', views.solicitud_producto_view, name='solicitud_producto'),
    path('welcome/solicitud_almacen_central/', views.solicitud_almacen_central, name='solicitud_almacen_central'),
    path('solicitud_exitosa/', views.solicitud_exitosa_view, name='solicitud_exitosa'),
    path('welcome/generar_reportes/', views.generar_reportes, name='generar_reportes'),
    path('registrar_productos/', views.registrar_productos, name='registrar_productos'),
]