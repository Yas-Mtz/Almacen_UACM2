from django.db import models

#modificación de rol, ya que solo habra 2 opciones
class Rol(models.Model):
    DOCENTE = 'docente'
    MANTENIMIENTO = 'mantenimiento'

    ROL_CHOICES = [
        (DOCENTE, 'Docente'),
        (MANTENIMIENTO, 'Personal de Mantenimiento'),
    ]

    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=255, choices=ROL_CHOICES)

#Creamos la clase persona con sus atributos y su respectiva clonación para hacer el prototipado
class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=255)

    def clone(self):
        # Crea una nueva instancia de Persona clonando los atributos del objeto actual
        new_persona = Persona(
            id_rol=self.id_rol,
            nombre=self.nombre,
            apellido_paterno=self.apellido_paterno,
            apellido_materno=self.apellido_materno,
            telefono=self.telefono,
            correo=self.correo,
            contrasena=self.contrasena
        )
        return new_persona

