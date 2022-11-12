from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Citas(models.Model):
    titulo =models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add = True)
    fecha_completada = models.DateTimeField(null = True, blank = True) 
    important = models.BooleanField(default=False)
    especialidad = models.CharField(max_length=100, null = True)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE) 



    def __str__(self):
        return self.titulo + ' - Por ' + self.usuario.username
        

class Especialidad(models.Model):
    Nombre_Especialidad = models.CharField(max_length=100, null = True)
