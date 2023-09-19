from .views import GestionDeUsuarios, vista2
from django.urls import path



urlpatterns = [
    path('GestionDeUsuarios/', GestionDeUsuarios, name='GestionDeUsuarios'),
    path('vista2/', vista2, name='vista2'),
]
