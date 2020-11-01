from django.db import models
from django.urls import reverse
import uuid


class PlacasMadre(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unico del producto')

    marca = models.CharField(max_length=100,help_text='Marca del producto')
    modelo = models.CharField(max_length=100)
    
    CATALOGO_FORMATO_PLACAMADRE = (
        ('seleccione','Seleccione'),
        ('ATX','ATX'),
        ('Mini ITX','Mini ITX'),
        ('Micro ATX','Micro ATX'),
    )

    formato = models.CharField(max_length=10,choices=CATALOGO_FORMATO_PLACAMADRE,blank=False,default='s',help_text='Formato de la Placa Madre')

    CATALOGO_PLATAFORMA_PLACAMADRE = (
        ('seleccione','Seleccione'),
        ('AMD','AMD'),
        ('Intel','Intel')
    )

    plataforma = models.CharField(max_length=10,choices=CATALOGO_PLATAFORMA_PLACAMADRE,blank=False,default='se',help_text='Plataforma de la Placa Madre')

    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='placasmadres/',null=False)
    
    precio = models.IntegerField(default=0)

    def __str__(self):
        return self.marca






