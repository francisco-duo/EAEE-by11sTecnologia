from django.db import models
from django.contrib.auth.models import User


class Agendamento(models.Model):
    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    paciente = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Paciente')
    especialidade = models.CharField(blank=True, null=True, max_length=255, verbose_name='Especialidade')
    dt_agendamento = models.DateField(blank=False, verbose_name='Data')
    frequencia = models.BooleanField(default=False, blank=True, verbose_name='Frequência')
