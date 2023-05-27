from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=50)
    apellido_profesor = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre_profesor}, {self.apellido_profesor} | Email {self.email}'

    
class Alumno(models.Model):
    nombre_alumno = models.CharField(max_length=50)
    apellido_alumno = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre_alumno}, {self.apellido_alumno}'
    
class Materias(models.Model):
    nombre_materia = models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.nombre_materia}'