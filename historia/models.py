from django.db import models

# Create your models here.


class mifotos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField('Foto',
        upload_to='imagenes/')
    descripcion = models.TextField(verbose_name='descripcion', null=True)

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - Descripción " + self.descripcion
        return fila


class Evento(models.Model):

    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    orden = models.CharField(max_length=10, verbose_name='ordenar', null=True)
    fecha = models.DateField()
    descripcion = models.TextField(verbose_name='Descripcion', null=True)
    imagen = models.ImageField(upload_to='images/', verbose_name='imagen')

    def __str__(self):
        fila = "Titulo: " + self.titulo  + " - Descripción " + self.descripcion
        # + "- imagen -" + format_html('<img scr={} />', self.imagen.url)
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()


class Participante(models.Model):
    participa = models.CharField(max_length=100, verbose_name='participa')
    nombres = models.CharField(max_length=100, verbose_name='nombres')
    fecha = models.DateField()
    descripcion = models.TextField(verbose_name='Descripcion', null=True)
    imagen = models.ImageField(upload_to='images/', verbose_name='imagen')

    def __str__(self):
        lista = "Participo en: " + self.participa + " - Nombres: " + \
            self.nombres + " - Descripción " + self.descripcion
        return lista
