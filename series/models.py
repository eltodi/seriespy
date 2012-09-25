# -*- coding=utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.ForeignKey(User)
    transmission_host = models.CharField(max_length=255, blank=True, null=True)
    transmission_port = models.IntegerField(default=9091)
    transmission_user = models.CharField(max_length=255, blank=True, null=True)
    transmission_password = models.CharField(max_length=255, blank=True, null=True)

class Genero(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

class Serie(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    productora = models.CharField(max_length=255, blank=True, null=True)
    genero = models.ManyToManyField(Genero, blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    imdb_id = models.CharField(max_length=255, blank=True, null=True)
    cover = models.URLField(blank=True, null=True)
    min_cover = models.URLField(blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    mini_plot = models.CharField(max_length=255, blank=True, null=True)
    rating = models.DecimalField(max_digits=10, decimal_places=1)

    def __unicode__(self):
        return self.titulo

class Episodio(models.Model):
    serie = models.ForeignKey(Serie)
    titulo = models.CharField(max_length=255)
    titulo_raw = models.CharField(max_length=255)
    temporada = models.IntegerField()
    numero = models.IntegerField()
    url_magnet = models.TextField(blank=True, null=True)
    #subtitulos = models.FileField(upload_to="subtitulos")

    def __unicode__(self):
        return "%s S%02dE%02d: %s" % (self.serie.titulo, self.temporada, self.numero, self.titulo)

    def numeracion_normalizada(self):
        return u'S%02dE%02d' % (self.temporada, self.numero)

class EpisodioUsuario(models.Model):
    user = models.ForeignKey(User)
    episodio = models.ForeignKey(Episodio)
    rating = models.DecimalField(max_digits=10, decimal_places=1)
    fecha_visto = models.DateTimeField(null=True, blank=True)
    fecha_descarga = models.DateTimeField(null=True, blank=True)

TIPOSEGUIMIENTO = (
    ('seguir','Seguir'),
    ('pte','Pendiente'),
    ('vista','Vista'),
)

class UsuarioSerie(models.Model):
    user = models.ForeignKey(User)
    serie = models.ForeignKey(Serie)
    tipo = models.CharField(max_length=50, choices=TIPOSEGUIMIENTO)
    desde = models.DateTimeField(auto_now_add=True)

class RegistroImportacion(models.Model):
    cuando = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_latest(cls):
        return cls.objects.all().order_by("-cuando")[0]