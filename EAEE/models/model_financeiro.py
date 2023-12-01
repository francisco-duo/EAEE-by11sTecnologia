from django.db import models
from django.contrib.auth.models import User


class RegistroFinanceiroTipoModel(models.Model):
    """
    registro_financeiro_tipo: varchar
    """

    registro_financeiro_tipo = models.CharField(blank=True, max_length=255)


class RegistroFinanceiroModel(models.Model):
    """
    registro_financeiro_funcionario: ForeignKey User
    registro_financeiro_valor: int
    registro_financeiro_tipo: ForeignKey
    """

    registro_financeiro_funcionario = models.ForeignKey(User, blank=True)
    registro_financeiro_valor = models.IntegerField(blank=True)
    registro_financeiro_tipo = models.ForeignKey(RegistroFinanceiroTipoModel)
