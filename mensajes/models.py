from django.db import models
from django.contrib.auth.models import User


class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name="remitente_set")
    destinatario = models.ForeignKey(User, related_name="destinatario_set")
    fecha = models.DateTimeField(auto_now_add=True)
    visto = models.BooleanField()
    texto = models.TextField()

    def __unicode__(self):
        return "mensaje de %s " % (self.remitente)


