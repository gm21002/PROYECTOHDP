from django.db import models

# Modelo de Clase Encuesta
class Encuesta(models.Model):    
    salest_encuesta = models.IntegerField()
    favor_encuesta = models.CharField(max_length=20)
    poraum_encuesta = models.IntegerField()
    ultaum_encuesta = models.CharField(max_length=20)    
    razon_encuesta = models.CharField(max_length=80)    
    comact_encuesta = models.CharField(max_length=20)    
    ventajas_encuesta = models.CharField(max_length=200)        
    desventajas_encuesta = models.CharField(max_length=200)        
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    # Definimos Clase anidada con el nombre de la base de datos
    class Meta:
        db_table = "encuestas"
        ordering = ['-created_at']

# Definimos modelo de usuarios para la Base de Datos
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=200)
    apellido_usuario = models.CharField(max_length=100)
    email_usuario = models.EmailField(max_length=50)
    password_usuario = models.CharField(max_length=80)
    edad_usuario = models.IntegerField()
    telefono_usuario = models.CharField(max_length=9)    

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # Definimos clase anidada con el nombre de la tabla
    class Meta:
        db_table = "usuarios"
        ordering = ['-created_at']

