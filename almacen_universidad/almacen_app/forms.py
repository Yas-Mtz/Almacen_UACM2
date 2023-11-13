from django import forms

#formulario para el registro de una une persona
class RegistroPersonaForm(forms.Form):
    nombre = forms.CharField(max_length=255)
    apellido_paterno = forms.CharField(max_length=255)
    apellido_materno = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=15)
    correo = forms.EmailField()
    contrasena = forms.CharField(max_length=255, widget=forms.PasswordInput())
