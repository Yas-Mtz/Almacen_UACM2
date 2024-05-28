# almacen_universidad/urls.py

from django.contrib import admin
from django.urls import path, include
from almacen_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Ruta para la URL raíz
    path('registrar_persona_prototipo/', views.registrar_persona_prototipo, name='registrar_persona_prototipo'),
    path('welcome/registrar_productos/', views.registrar_productos, name='registrar_productos'),
    path('welcome/generar_reportes/', views.generar_reportes, name='generar_reportes'),
    path('welcome/solicitud_productos_almacen/', views.solicitar_almacen_central, name='solicitud_productos_almacen'),
    path('welcome/solicitud_productos/', views.solicitar_productos, name='solicitud_productos'),
]
