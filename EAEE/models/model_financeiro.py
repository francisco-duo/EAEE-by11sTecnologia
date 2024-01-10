from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Financeiro
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

    class Meta:
        verbose_name = "Financeiro"
        verbose_name_plural = "Financeiro"

    registro_financeiro_funcionario = models.ForeignKey(User, blank=True, on_delete=models.DO_NOTHING)
    registro_financeiro_valor = models.CharField(max_length=255, blank=True)
    registro_financeiro_destino = models.CharField(max_length=255, blank=True)
    registro_financeiro_tipo = models.ForeignKey(RegistroFinanceiroTipoModel, on_delete=models.DO_NOTHING)
    registro_financeiro_dt = models.DateTimeField(verbose_name='Data')
    data_filtro = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.registro_financeiro_destino

    def save(self, *args, **kwargs):
        self.data_filtro = self.registro_financeiro_dt.date()
        super().save(*args, **kwargs)