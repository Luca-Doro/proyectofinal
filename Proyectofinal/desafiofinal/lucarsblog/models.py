from django.db import models

# Create your models here.

class automovil(models.Model):
    
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)


class deportivos(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)


class suv(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)


class pickup(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    

