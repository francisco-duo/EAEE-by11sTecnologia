from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from EAEE.models import model_pacientes


class Devolutiva(models.Model):
    class Meta:
        verbose_name = "Devolutiva"
        verbose_name_plural = "Devolutiva"

    dt_registro = models.DateTimeField(default=timezone.now, verbose_name='Data', blank=True, null=True)
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    anexo = models.FileField(blank=True, null=True, upload_to='paciente/documentos/exames', verbose_name='Anexo')
    dt_devolutiva = models.DateField(blank=True, null=True, verbose_name='Data')
    para = models.CharField(blank=True, null=True, max_length=255, verbose_name='Para')
    sintese = models.TextField(blank=True, null=True, verbose_name='Síntese')


class ReunioesExternas(models.Model):
    class Meta:
        verbose_name = "Reuniões Externas"
        verbose_name_plural = "Reuniões Externas"

    dt_registro = models.DateTimeField(default=timezone.now, verbose_name='Data', blank=True, null=True)
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    anexo = models.FileField(blank=True, null=True, upload_to='paciente/documentos/exames', verbose_name='Anexo')
    dt_devolutiva = models.DateField(blank=True, null=True, verbose_name='Data')
    participantes = models.TextField(blank=True, null=True, verbose_name='Participantes')
    sintese = models.TextField(blank=True, null=True, verbose_name='Síntese')


class Encaminhamento(models.Model):
    class Meta:
        verbose_name = "Encaminhamento"
        verbose_name_plural = "Encaminhamento"

    dt_registro = models.DateTimeField(default=timezone.now, verbose_name='Data', blank=True, null=True)
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    anexo = models.FileField(blank=True, null=True, upload_to='paciente/documentos/exames', verbose_name='Anexo')
    dt_devolutiva = models.DateField(blank=True, null=True, verbose_name='Data')
    sintese = models.TextField(blank=True, null=True, verbose_name='Observações')


class EvolucaoDiaria(models.Model):
    class Meta:
        verbose_name = "Evolução Diária"
        verbose_name_plural = "Evolução Diária"

    dt_registro = models.DateTimeField(default=timezone.now, verbose_name='Data', blank=True, null=True)
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    anexo = models.FileField(blank=True, null=True, upload_to='paciente/documentos/exames', verbose_name='Anexo')
    dt_devolutiva = models.DateField(blank=True, null=True, verbose_name='Data')
    sintese = models.TextField(blank=True, null=True, verbose_name='Síntese')


class SupervisaoMultiprofissional(models.Model):
    class Meta:
        verbose_name = "Supervisao Multiprofissional"
        verbose_name_plural = "Supervisao Multiprofissional"

    dt_registro = models.DateTimeField(default=timezone.now, verbose_name='Data', blank=True, null=True)
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    anexo = models.FileField(blank=True, null=True, upload_to='paciente/documentos/exames', verbose_name='Anexo')
    dt_devolutiva = models.DateField(blank=True, null=True, verbose_name='Data')
    especialista = models.TextField(blank=True, null=True, verbose_name='Especialistas')
    observacao = models.TextField(blank=True, null=True, verbose_name='Observações')
    plano_de_acao = models.TextField(blank=True, null=True, verbose_name='Plano de Ação')
