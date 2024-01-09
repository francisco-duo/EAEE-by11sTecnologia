from django.db import models

from django.utils import timezone


class PacienteModel(models.Model):
    """
    """
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Paciente"

    # Campos do paciente
    paciente_nome = models.CharField(blank=True, null=True, max_length=255, verbose_name='Nome')
    paciente_foto = models.ImageField(blank=True, null=True, upload_to='paciente/fotos/',)
    paciente_dt_nascimento = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    paciente_identidade = models.FileField(blank=True, null=True, upload_to='paciente/documentos/identificacao', verbose_name='Identidade')
    paciente_exame = models.FileField(blank=True, null=True, upload_to='paciente/documentos/exames', verbose_name='Exame_1')
    paciente_exame_2 = models.FileField(blank=True, null=True, upload_to='paciente/documentos/exames', verbose_name='Exame_2')
    paciente_exame_3 = models.FileField(blank=True, null=True, upload_to='paciente/documentos/exames', verbose_name='Exame_3')

    # Data de inscrição na clínica
    paciente_dt_inscricao = models.DateTimeField(default=timezone.now, verbose_name='Data de Inscrição')  # DateTime

    def __str__(self, ):
        return self.paciente_nome


class InformacoesComplementares(models.Model):

    class Meta:
        verbose_name = "Informações Complemetares"
        verbose_name_plural = "Informações Complementares"

    paciente = models.ForeignKey(PacienteModel, on_delete=models.CASCADE, verbose_name='Paciente')
    escola = models.CharField(blank=True, null=True, max_length=255)
    serie = models.CharField(blank=True, null=True, max_length=255)
    turno = models.CharField(blank=True, null=True, max_length=255)
    gravidez = models.CharField(blank=True, null=True, max_length=255)
    fatos_marcantes = models.TextField(blank=True, null=True)
    condicoes_emocionais = models.TextField(blank=True, null=True)
    pos_parto = models.TextField(blank=True, null=True)
    parto = models.CharField(blank=True, null=True, max_length=255)
    semanas = models.CharField(blank=True, null=True, max_length=255)
    peso = models.CharField(blank=True, null=True, max_length=255)
    altura = models.CharField(blank=True, null=True, max_length=255)
    cuidados_parto = models.CharField(blank=True, null=True, max_length=255)
    apgar1 = models.CharField(blank=True, null=True, max_length=255)
    apgar5 = models.CharField(blank=True, null=True, max_length=255)
    succao = models.CharField(blank=True, null=True, max_length=255)
    leite_marterno = models.CharField(blank=True, null=True, max_length=255)
    usou_mamadeira = models.CharField(blank=True, null=True, max_length=255)
    alimento_atual = models.CharField(blank=True, null=True, max_length=255)
    recebe_ajuda = models.CharField(blank=True, null=True, max_length=255)
    sono = models.CharField(blank=True, null=True, max_length=255)
    baba = models.CharField(blank=True, null=True, max_length=255)
    acorda = models.CharField(blank=True, null=True, max_length=255)
    fala_dormindo = models.CharField(blank=True, null=True, max_length=255)
    dorme_sozinho = models.CharField(blank=True, null=True, max_length=255)
    horario_de_dormir = models.CharField(blank=True, null=True, max_length=255)
    esfincteres = models.CharField(blank=True, null=True, max_length=255)
    fobias = models.CharField(blank=True, null=True, max_length=255)
    mora = models.CharField(blank=True, null=True, max_length=255)


class TipoDeVinculoComPacienteModels(models.Model):
    class Meta:
        verbose_name = "Responsável"
        verbose_name_plural = "Responsável"

    paciente = models.ForeignKey(PacienteModel, on_delete=models.CASCADE, verbose_name='Paciente')
    paciente_filiacao_nome = models.CharField(blank=True, null=True, max_length=255, verbose_name='Nome')
    paciente_filiacao_tipo_vinculo = models.CharField(blank=True, null=True, max_length=255, verbose_name='Tipo de Vinculo')
    paciente_filiacao_email = models.EmailField(blank=True, null=True, verbose_name='Email')
    paciente_filiacao_dt_nascimento = models.DateField(blank=True, null=True, )
    paciente_filiacao_contato_telefone_pessoal = models.CharField(blank=True, null=True, max_length=255, verbose_name='Contato Pessoal')
    paciente_filiacao_contato_telefone_empresa = models.CharField(blank=True, null=True, max_length=255, verbose_name='Contato Profissional')
    paciente_filiacao_cpf = models.CharField(blank=True, null=True, max_length=255, verbose_name='Identidade')
    paciente_filiacao_nacionalidade = models.CharField(blank=True, null=True, max_length=255, verbose_name='Nacionalidade')
    paciente_filiacao_profissao = models.CharField(blank=True, null=True, max_length=255, verbose_name='Profissão')
    paciente_filiacao_estado_civil = models.CharField(blank=True, null=True, max_length=255, verbose_name='Estado Civil')
    paceinte_filiacao_endereco = models.CharField(blank=True, null=True, max_length=255, verbose_name='Endereço')
    paceinte_filiacao_cep = models.CharField(blank=True, null=True, max_length=255, verbose_name='Endereço')
    paceinte_filiacao_comprovante_residencia = models.FileField(blank=True, null=True, upload_to='files/filiado/comprovante_de_residencia', verbose_name='Comprovante de Residencia')

    def __str__(self, ):
        return self.paciente_filiacao_nome

