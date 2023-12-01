from django.db import models


class ExamePacienteModel(models.Model):
    """
        exame_paciente_nome: varchar
        exame_paciente_dt_recebimento: date
    """

    ...


class PacienteModel(models.Model):
    """
        paciente_nome: varchar
        paciente_dt_nasc: date
        paciente_responsavel_nome: varchar
        paciente_responsavel_email: emailField
        paciente_responsavel_contato: varchar
        paciente_responsavel_cpf: varchar --> Validar
        paciente_exams: file --> ForeignKey
        paciente_foto: image
    """

    paciente_nome = models.Charfiled(blank=True)
    paciente_dt_nasc = models.DateField(blank=True)
    paciente_responsavel_nome = models.CharField(blank=True, max_length=255)
    paciente_responsavel_email = models.EmailField(blank=True)
    paciente_responsavel_contato = models.CharField(blank=True, max_length=255)
    paciente_responsavel_cpf = models.CharField(blank=True, max_length=255)
    paciente_exams = models.FileField(upload_to='/files/')
    paciente_foto = models.ImageField(upload_to='/media/')
