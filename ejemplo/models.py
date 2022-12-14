from django.db import models

class Familiar(models.Model):
  
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()

    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class Automovil(models.Model):
  
    propietario = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    patente = models.CharField(max_length=100)
    
    def __str__(self):
      return f"{self.propietario}, {self.marca}, {self.color}, {self.patente}"

class Mascota(models.Model):
  
    nombre = models.CharField(max_length=100)
    propietario = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    
    def __str__(self):
      return f"{self.propietario}, {self.nombre}, {self.raza}, {self.edad}"