from django import forms

class RegistroPersonaForm(forms.Form):
    id_rol = forms.CharField(max_length=255)
    nombre = forms.CharField(max_length=255)
    apellido_paterno = forms.CharField(max_length=255)
    apellido_materno = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=15)
    correo = forms.EmailField()
    contrasena = forms.CharField(max_length=255, widget=forms.PasswordInput())