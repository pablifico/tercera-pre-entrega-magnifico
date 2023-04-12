from django.db import models

# Create your models here.

class Jugador(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    posicion = models.CharField(max_length=20)
    
    def __str__(self):
        return f'El jugador se llama {self.nombre}, tiene {self.edad} años, nacio en {self.fecha_nacimiento} y juega de {self.posicion}'
    
