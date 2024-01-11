from django.db import models
from .model_pacientes import PacienteModel


class Agendamento(models.Model):
    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    paciente = models.ForeignKey(PacienteModel, on_delete=models.DO_NOTHING, verbose_name='Paciente')
    especialidade = models.CharField(blank=True, null=True, max_length=255, verbose_name='Especialidade')
    dt_agendamento = models.DateField(blank=False, verbose_name='Data')
    presente = models.BooleanField(default=False, blank=True, verbose_name='Presente')
    falta = models.BooleanField(default=False, blank=True, verbose_name='Falta')
    reposicao = models.BooleanField(default=False, blank=True, verbose_name='Reposição')
    justificativa = models.TextField(blank=True, null=True, verbose_name='Justificativa')
