from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PacienteModel(models.Model):
    """
    """

    # Campos do paciente
    paciente_nome = models.CharField(blank=True, max_length=255, verbose_name='Nome')
    paciente_foto = models.ImageField(blank=False, upload_to='paciente/fotos/',)
    paciente_dt_nascimento = models.DateField(blank=False, verbose_name='Data de Nascimento')
    paciente_identidade = models.FileField(blank=False, upload_to='paciente/documentos/identificacao', verbose_name='Identidade')
    paciente_exame = models.FileField(blank=False, upload_to='paciente/documentos/exames', verbose_name='Exame_1')
    paciente_exame_2 = models.FileField(blank=False, upload_to='paciente/documentos/exames', verbose_name='Exame_2')
    paciente_exame_3 = models.FileField(blank=False, upload_to='paciente/documentos/exames', verbose_name='Exame_3')

    # Data de inscrição na clínica
    paciente_dt_inscricao = models.DateTimeField(default=timezone.now, verbose_name='Data de Inscrição')  # DateTime


class TipoDeVinculoComPacienteModels(models.Model):
    paciente = models.ManyToManyField(PacienteModel, verbose_name='Responsável')
    paciente_filiacao_nome = models.CharField(blank=False, max_length=255, verbose_name='Nome')
    paciente_filiacao_tipo_vinculo = models.CharField(blank=False, max_length=255, verbose_name='Tipo de Vinculo')
    paciente_filiacao_email = models.EmailField(blank=False, verbose_name='Email')
    paciente_filiacao_dt_nascimento = models.DateField(blank=False, )
    paciente_filiacao_contato_telefone_pessoal = models.CharField(blank=False, max_length=255, verbose_name='Contato Pessoal')
    paciente_filiacao_contato_telefone_empresa = models.CharField(blank=False, max_length=255, verbose_name='Contato Profissional')
    paciente_filiacao_cpf = models.CharField(blank=False, max_length=255, verbose_name='Identidade')
    paciente_filiacao_nacionalidade = models.CharField(blank=False, max_length=255, verbose_name='Nacionalidade')
    paciente_filiacao_profissao = models.CharField(blank=False, max_length=255, verbose_name='Profissão')
    paciente_filiacao_estado_civil = models.CharField(blank=False, max_length=255, verbose_name='Estado Civil')
    paceinte_filiacao_endereco = models.CharField(blank=False, max_length=255, verbose_name='Endereço')
    paceinte_filiacao_comprovante_residencia = models.FileField(blank=False, upload_to='files/filiado/comprovante_de_residencia', verbose_name='Comprovante de Residencia')
