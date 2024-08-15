from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return "{} | ID: {}".format(self.nombre, self.id)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return "Nombre completo del alumno: {} {} | Dirección Email: {}".format(self.nombre,self.apellido,self.email)

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    apellido = models.CharField(max_length=30)
    
    def __str__(self):
        return "Nombre completo del profesor: {} {}".format(self.nombre,self.apellido)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField(max_length=40)
    entregado = models.BooleanField(max_length=30)

    def __str__(self):
        return "ID de entrega: {}  |  (click para más información)".format(self.nombre)
