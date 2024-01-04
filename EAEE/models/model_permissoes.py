from django.db import models
from django.contrib.auth.models import User


class PermissoesModel(models.Model):
    # Adicione sua nova coluna aqui
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    permissao = models.CharField(max_length=100, blank=True, null=True)
