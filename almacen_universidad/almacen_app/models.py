from django.db import models

class Rol(models.Model):
    #Representación de los roles 
    DOCENTE = 'docente'
    MANTENIMIENTO = 'mantenimiento'

    ROL_CHOICES = [
        (DOCENTE, 'Docente'),
        (MANTENIMIENTO, 'Personal de Mantenimiento'),
    ]

    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=255, choices=ROL_CHOICES)

class Persona(models.Model):
    # Modelo de representación de una persona.
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

# Implementaremos la clase de almacen para la solicitud de productos a futuro de los 5 planteles

class Alamcen(models.Model):
      NOMBRES_ALMACENES = [
          ('cuatepec', 'Almacen de Cuatepec'),
          ('san_lorenzo', 'Almacen de San Lorenzo'),
          ('casa_libertad', 'Almacen de Casa Libertad'),
          ('del_valle', 'Almacen del Valle'),
          ('centro_historico', 'Almacen de Centro Histórico'),
      ]

     nombre = models.CharField(max_length=20, choices=NOMBRES_ALMACENES, unique=True

    def __str__(self):
        return dict(self.NOMBRES_ALMACENES)[self.nombre]
