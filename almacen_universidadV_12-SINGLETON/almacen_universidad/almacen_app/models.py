from django.db import models


class Rol(models.Model):
    DOCENTE = 'docente'
    MANTENIMIENTO = 'mantenimiento'

    ROL_CHOICES = [
        (DOCENTE, 'Docente'),
        (MANTENIMIENTO, 'Personal de Mantenimiento'),
    ]

    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=255, choices=ROL_CHOICES)


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

# PATRON SINGLETON


class Singleton:  # Declaración de clase
    _instance = None  # Variable de clase para almacenar la única instancia de la clase

    def __new__(cls):  # método "__new__" que se llama al crear una nueva instancia en la clase ( verifica si ya existe una instancia de la clase (cls._instance))
        if cls._instance is None:  # verificación de clase

            # si no hay instancia, crea una nueva utilizando "__new__"
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance  # devuelve la instancia existente o creada
