from django.urls import path
from . import views

urlpatterns = [
   path('', views.login_view, name='login'),  # Cambia la ruta de '' a 'login/'
    path('welcome/', views.welcome_view, name='welcome'),
    # ... otras rutas ...
]