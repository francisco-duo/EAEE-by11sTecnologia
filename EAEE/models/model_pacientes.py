from django.db import models

from django.utils import timezone


class PacienteModel(models.Model):
    """
    """
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Paciente"

    # Campos do paciente
    paciente_nome = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Nome')
    paciente_foto = models.ImageField(
        blank=True, null=True, upload_to='paciente/fotos/',
        verbose_name='Foto do paciente'
    )
    paciente_dt_nascimento = models.DateField(
        blank=True, null=True, verbose_name='Data de Nascimento')
    paciente_identidade = models.FileField(blank=True, null=True,
                                           upload_to='paciente/documentos/identificacao', verbose_name='Identidade')
    paciente_medicacao = models.TextField(
        blank=True, null=True, verbose_name='O paciente faz uso de medicação?'
    )
    paciente_exame = models.FileField(
        blank=True, null=True, upload_to='paciente/documentos/exames', verbose_name='Exame'
    )
    paciente_exame_2 = models.FileField(
        blank=True, null=True, upload_to='paciente/documentos/exames', verbose_name='Exame'
    )
    paciente_exame_3 = models.FileField(
        blank=True, null=True, upload_to='paciente/documentos/exames', verbose_name='Exame'
    )

    # Data de inscrição na clínica
    paciente_dt_inscricao = models.DateTimeField(
        default=timezone.now, verbose_name='Data de Inscrição')  # DateTime

    def __str__(self, ):
        return self.paciente_nome


class InformacoesComplementares(models.Model):

    class Meta:
        verbose_name = "Informações Complemetares"
        verbose_name_plural = "Informações Complementares"

    paciente = models.ForeignKey(
        PacienteModel, on_delete=models.CASCADE, verbose_name='Paciente')
    escola = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Escola em que estuda?')
    serie = models.CharField(blank=True, null=True,
                             max_length=255, verbose_name='Série')
    turno = models.CharField(blank=True, null=True,
                             max_length=255, verbose_name='Turno')
    gravidez = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Gravidez desejada?')
    fatos_marcantes = models.TextField(
        blank=True, null=True, verbose_name='Doenças ou fatos marcantes?')
    condicoes_emocionais = models.TextField(
        blank=True, null=True, verbose_name='Condições emocionais')
    pos_parto = models.TextField(
        blank=True, null=True, verbose_name='Como foi o pós-parto?')
    parto = models.CharField(blank=True, null=True,
                             max_length=255, verbose_name='Normal ou Cesárea')
    semanas = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Nasceu com quantas semanas?')
    peso = models.CharField(blank=True, null=True,
                            max_length=255, verbose_name='Peso')
    altura = models.CharField(blank=True, null=True,
                              max_length=255, verbose_name='Altura')
    cuidados_parto = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Necessitou de cuidados especiais?')
    apgar1 = models.CharField(blank=True, null=True,
                              max_length=255, verbose_name='Apgar 1º minuto')
    apgar5 = models.CharField(blank=True, null=True,
                              max_length=255, verbose_name='Apgar 5º minuto')
    succao = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='1ª sucção (amamentação)')
    leite_marterno = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Leite marteno exclusivo até que idade?')
    usou_mamadeira = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Usou mamadeira?')
    alimento_atual = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Alimentação atual (preferências)')
    come_sem_derramar = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Come sem derramar?')
    recebe_ajuda = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Recebe ajuda?')
    sono = models.CharField(blank=True, null=True,
                            max_length=255, verbose_name='Sono agitado?')
    baba = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Baba durante a noite?')
    acorda = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Acorda durante a noite?')
    fala_dormindo = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Fala dormindo?')
    dorme_sozinho = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Dorme sozinho?')
    horario_de_dormir = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Horário que costuma dormir')
    esfincteres = models.CharField(blank=True, null=True, max_length=255,
                                   verbose_name='Teve/ tem dificuldade para adquirir o controle dos esfíncteres?')
    fobias = models.CharField(blank=True, null=True,
                              max_length=255, verbose_name='Medou ou fobias?')
    mora = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Quem mora com a criança?')


class TipoDeVinculoComPacienteModels(models.Model):
    class Meta:
        verbose_name = "Responsável"
        verbose_name_plural = "Responsável"

    paciente = models.ManyToManyField(PacienteModel, verbose_name='Paciente')
    paciente_filiacao_nome = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Nome')
    paciente_filiacao_tipo_vinculo = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Tipo de Vinculo')
    paciente_filiacao_email = models.EmailField(
        blank=True, null=True, verbose_name='Email')
    paciente_filiacao_dt_nascimento = models.DateField(blank=True, null=True, )
    paciente_filiacao_contato_telefone_pessoal = models.CharField(blank=True,
                                                                  null=True, max_length=255, verbose_name='Contato Pessoal')
    paciente_filiacao_contato_telefone_empresa = models.CharField(blank=True,
                                                                  null=True, max_length=255, verbose_name='Contato Profissional')
    paciente_filiacao_cpf = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='Identidade')
    paciente_filiacao_documento = models.CharField(
        blank=True, null=True, max_length=255, verbose_name='CPF')
    paciente_filiacao_nacionalidade = models.CharField(blank=True, null=True,
                                                       max_length=255, verbose_name='Nacionalidade')
    paciente_filiacao_profissao = models.CharField(blank=True, null=True,
                                                   max_length=255, verbose_name='Profissão')
    paciente_filiacao_estado_civil = models.CharField(blank=True, null=True,
                                                      max_length=255, verbose_name='Estado Civil')
    paceinte_filiacao_endereco = models.CharField(blank=True, null=True,
                                                  max_length=255, verbose_name='Endereço')
    paceinte_filiacao_cep = models.CharField(blank=True, null=True,
                                             max_length=255, verbose_name='Endereço')
    paceinte_filiacao_comprovante_residencia = models.FileField(blank=True,
                                                                null=True, upload_to='files/filiado/comprovante_de_residencia',
                                                                verbose_name='Comprovante de Residencia')
    paceinte_filiacao_contrato = models.FileField(blank=True,
                                                  null=True, upload_to='files/filiado/comprovante_de_residencia',
                                                  verbose_name='Contrato')
    paceinte_filiacao_contrato_2 = models.FileField(blank=True,
                                                  null=True, upload_to='files/filiado/comprovante_de_residencia',
                                                  verbose_name='Contrato')

    def __str__(self, ):
        return self.paciente_filiacao_nome
