from django.db import models

"""
from django.contrib.auth.models import User



# Create your models here.
#manejo de usuarios perzonalizados
class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #Agregamos datos
    contacto=models.CharField(max_length=12,default="")
    region=models.CharField(max_length=20,default="Metropolitana")
    vivienda=models.CharField(max_length=20,default="")
    perfil=models.CharField(max_length=20,default="Adoptante")
    


#modelo de la mascota
class Mascota (models.Model):
    codigoMascota=models.AutoField(primary_key=True)
    fotoMascota = models.ImageField(upload_to="fotos/")
    nombreMascota=models.CharField(max_length=20,verbose_name="Nombre Mascota")
    razaMascota=models.CharField(max_length=30,default="",verbose_name="Raza Mascota")
    descripcionMascota=models.CharField(max_length=50,default="",verbose_name="Descripcion")
    estado=models.CharField(max_length=20,verbose_name="Estado")


"""



"""
class Mascota(models.Model):
    codigoMascota=models.AutoField(primary_key=True)
    nombreMascota=models.CharField(max_length=20,default="")
    razaMascota=models.CharField(max_length=30,default="")
    descripcionMascota=models.CharField(max_length=50,default="")
    estado=models.CharField(max_length=20,default="Rescatado")
"""

"""      
class Fomulario(models.Model):
    rut=models.CharField(primary_key=True, max_length=9,default="")
    nombre=models.CharField(max_length=30,default="")
    correo=models.EmailField(max_length=30,default="")
    username=models.CharField(max_length=30,default="")
    password=models.CharField(max_length=30,default="")
"""