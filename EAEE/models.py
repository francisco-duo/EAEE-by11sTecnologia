from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ComunicadoModel(models.Model):
    """
    comunicado_usuario: ForeignKey User
    comunicado_mensagem: TextField
    comunicado_dt: Date
    """

    comunicado_usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comunicado_mensagem = models.TextField()
    comunicado_dt = models.DateTimeField(default=timezone.now, verbose_name='Data')

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

    registro_financeiro_funcionario = models.ForeignKey(User, blank=True, on_delete=models.DO_NOTHING)
    registro_financeiro_valor = models.CharField(max_length=255 ,blank=True)
    registro_financeiro_tipo = models.ForeignKey(RegistroFinanceiroTipoModel, on_delete=models.DO_NOTHING)
    registro_financeiro_dt = models.DateTimeField(default=timezone.now, verbose_name='Data')

# Paciente


# class ExamePacienteModel(models.Model):
#     """
#         exame_paciente_nome: varchar
#         exame_paciente_dt_recebimento: date
#     """

#     ...


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

    paciente_nome = models.CharField(max_length=255, blank=True)
    paciente_dt_nasc = models.DateField(blank=True)
    paciente_responsavel_nome = models.CharField(blank=True, max_length=255)
    paciente_responsavel_email = models.EmailField(blank=True)
    paciente_responsavel_contato = models.CharField(blank=True, max_length=255)
    paciente_responsavel_cpf = models.CharField(blank=True, max_length=255)
    paciente_exams = models.FileField(upload_to='files/')
    paciente_foto = models.ImageField(upload_to='photos/')

# Registro de Pacientes


class PacienteRegistroModel(models.Model):
    """
        paciente_registro_paciente: ForeignKey Paciente
        paciente_registro_queixa: TextField
        paciente_registro_historico: ForeignKey Exame
        paciente_registro_procedimento_avaliativo: TextField
        paciente_registro_observacao_clinica: TextField
        paciente_registro_resultado: TextField
        paciente_registro_conclusao: TextField
    """
    paciente_registro_paciente =  models.ForeignKey(User, on_delete=models.DO_NOTHING)  # : ForeignKey Paciente
    paciente_registro_queixa = models.TextField()  # : TextField
    paciente_registro_historico = models.ForeignKey(PacienteModel, on_delete=models.CASCADE)  # : ForeignKey Exame
    paciente_registro_procedimento_avaliativo = models.TextField()  # : TextField
    paciente_registro_observacao_clinica = models.TextField()  # : TextField
    paciente_registro_resultado = models.TextField()  # : TextField
    paciente_registro_conclusao = models.TextField()  # : TextField
    paciente_registro_dt_criacao = models.DateTimeField(default=timezone.now, verbose_name='Data')  # DateTime
