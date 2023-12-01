from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ComunicadoModel(models.Model):
    """
    comunicado_usuario: ForeignKey User
    comunicado_mensagem: TextField
    comunicado_dt: Date
    """

    comunicado_usuario = models.ForeignKey(User)
    comunicado_mensagem = models.TextField()
    comunicado_dt = models.DateTimeField(default=timezone.now, verbose_name='Data')
