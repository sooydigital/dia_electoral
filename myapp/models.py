from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

import uuid
from django.db import models

# Register your models here.


# Create your models here.
class Departamento(models.Model):
    name = models.CharField(
        max_length=1024,
        verbose_name="nombre del departamento"
    )
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Departamento, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)

class Municipio(models.Model):
    departamento = models.ForeignKey(
        Departamento,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=1024,
        verbose_name="nombre del municipio"
    )
    slug = models.SlugField()

    longitude = models.CharField(
        max_length=1024,
        verbose_name="longitude",
        blank=True,
        null=True,

    )
    latitude = models.CharField(
        max_length=1024,
        verbose_name="latitude",
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Municipio, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)

class Comuna(models.Model):
    municipio = models.ForeignKey(
        Municipio,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=1024,
        verbose_name="nombre de comuna"
    )
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Comuna, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)

class Barrio(models.Model):
    municipio = models.ForeignKey(
        Municipio,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )    
    
    comuna = models.ForeignKey(
        Comuna,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=1024,
        verbose_name="nombre del barrio"
    )
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Barrio, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)

class PuestoVotacion(models.Model):
    departamento = models.ForeignKey(
        Departamento,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    municipio = models.ForeignKey(
        Municipio,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    barrio = models.ForeignKey(
        Barrio,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    nombre = models.CharField(
        max_length=1024,
        verbose_name="Nombre Puesto de Votación",
        blank=True,
        null=True,
    )
    direccion = models.CharField(
        max_length=1024,
        verbose_name="Dirección",
        blank=True,
        null=True,
    )
    latitude = models.CharField(
        max_length=1024,
        verbose_name="latitude",
        blank=True,
        null=True,
    )
    longitude = models.CharField(
        max_length=1024,
        verbose_name="longitude",
        blank=True,
        null=True,
    )

    link = models.URLField(default=None, null=True, blank=True)

    def __str__(self):
        return '{} -- {} -- {}'.format(self.nombre, self.direccion, self.municipio)

class Mesa(models.Model):
    puesto_votacion = models.ForeignKey(
        PuestoVotacion,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    numero = models.PositiveIntegerField()


    def __str__(self):
        if  self.puesto_votacion:
            return '{} - {}'.format(self.numero, self.puesto_votacion.nombre)
        else:
            return '{} - {}'.format(self.numero, '')


class Candidato(models.Model):

    TYPE_CANDIDATURA = (
        ('Alcaldía', 'Alcaldía'),
        ('Gobernación', 'Gobernación'),
        ('Concejo', 'Concejo'),
        ('Asamblea', 'Asamblea'),
    )
    candidatura = models.CharField(max_length=20, choices=TYPE_CANDIDATURA)

    nombre = models.CharField(
        max_length=1024,
        verbose_name="nombre del candidato"
    )
    partido = models.CharField(
        max_length=1024,
        verbose_name="nombre del partido",
        null=True,
        default=None,
    )
    numero = models.CharField(
        max_length=3,
        verbose_name="numero",
        null=True,
        default=None,
    )


    def __str__(self):
        return '{}'.format(self.nombre)

class Registro(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    cantidato = models.ForeignKey(
        Candidato,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    testigo = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    puesto_votacion = models.ForeignKey(
        PuestoVotacion,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    numero_de_votos = models.PositiveIntegerField(default=None, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)