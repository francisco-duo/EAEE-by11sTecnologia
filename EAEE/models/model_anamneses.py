from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from EAEE.models import model_pacientes


class Psicopedagogia(models.Model):
    class Meta:
        verbose_name = "Psicopedagogia"
        verbose_name_plural = "Psicopedagogia"

    dt_registro = models.DateTimeField(default=timezone.now, verbose_name='Data')
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    idade_que_comecou_a_frequentar_escola = models.CharField(blank=False, max_length=255)
    como_foi_adaptacao = models.TextField(blank=False)
    reprovou = models.CharField(blank=False, max_length=255)
    ralacao_professores_colegas = models.TextField(blank=False)
    motivado_escola = models.CharField(blank=False, max_length=255)
    falta_assiduo = models.TextField(blank=False)
    realiza_atividades_com_satisfacao = models.CharField(blank=False, max_length=255)
    precisa_ajuda = models.TextField(blank=False)
    predilecao_matematica_portugues = models.TextField(blank=False)
    dificuldades_aprendizagem = models.TextField(blank=False)
    antecedentes_com_dificuldade = models.TextField(blank=False)
    queixas_comuns_escola = models.TextField(blank=False)
    fala_compreensivel = models.TextField(blank=False)
    # troca_ou_omissao_fonemas = models.TextField(blank=False)
    # conta_historia = models.TextField(blank=False)
    corporalmente_desenvolto = models.CharField(blank=False, max_length=255)
    anda_bicicleta = models.CharField(blank=False, max_length=255)
    organizado = models.CharField(blank=False, max_length=255)
    ajuda_em_casa = models.TextField(blank=False)
    censurado = models.TextField(blank=False)
    brinquedos_favorito = models.TextField(blank=False)
    gosta_desenhar = models.TextField(blank=False)
    uso_de_eletronicos = models.TextField(blank=False)
    horas_livres = models.TextField(blank=False)
    potencialidades_marcantes = models.TextField(blank=False)
    fragilidades_evidentes = models.TextField(blank=False)

    def __str__(self, ):
        return self.paciente


class Psicologia(models.Model):
    class Meta:
        verbose_name = "Psicologia"
        verbose_name_plural = "Psicologia"
    dt_registro = models.DateTimeField(default=timezone.now, verbose_name='Data')
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    numero_irmaos = models.CharField(blank=False, max_length=255)
    reacao_nascimento_irmao = models.TextField(blank=False)
    relacionamento_irmaos = models.TextField(blank=False)
    relacionamento_pais = models.TextField(blank=False)
    relacionamento_familia = models.TextField(blank=False)
    personalidade = models.CharField(blank=False, max_length=255)
    comportamento_roer_unhas = models.TextField(blank=False)
    humor_habitual = models.TextField(blank=False)
    brinca_sozinho_ou_grupo = models.TextField(blank=False)
    estranha_mudancas_ambiente = models.TextField(blank=False) 
    aceita_seguir_comandos = models.TextField(blank=False)
    brincadeiras_brinquedo_favorito = models.TextField(blank=False)
    gosta_de_musicas = models.TextField(blank=False)
    baste_cabeca_na_parede = models.TextField(blank=False)
    atitudes_desse_habito = models.TextField(blank=False)
    reprovou_na_escola = models.TextField(blank=False)
    relacionamento_colegas = models.TextField(blank=False)
    relacionamento_professores = models.TextField(blank=False)
    idade_desfralde = models.TextField(blank=False)
    dificuldades_desfraude = models.TextField(blank=False)
    higiene_sozinho = models.TextField(blank=False)
    idade_higiene_sozinho = models.TextField(blank=False)
    problema_na_fala = models.TextField(blank=False)
    troca_letras = models.TextField(blank=False)
    acorda_vai_para_cama_dos_pais = models.TextField(blank=False)
    dorme_sozinho = models.TextField(blank=False)
    objeto_para_dormir = models.TextField(blank=False)
    urina_na_cama = models.TextField(blank=False)
    horario_para_refeicoes = models.TextField(blank=False)
    refeicoes_em_familia = models.TextField(blank=False)
    local = models.TextField(blank=False)
    assiste_enquanto_come = models.TextField(blank=False)
    como_se_alimenta = models.TextField(blank=False)
    seletividade_alimentar = models.TextField(blank=False)
    curiosidade_sexual = models.TextField(blank=False)
    atitude_dos_pais = models.TextField(blank=False)
    informacoes_sexuais = models.TextField(blank=False)
    tratamento_medico = models.TextField(blank=False)
    internado = models.TextField(blank=False)
    motivo_internação = models.TextField(blank=False)
    operado = models.TextField(blank=False)
    idade_operado = models.TextField(blank=False)
    adoece_facilmente = models.TextField(blank=False)
    acompanhamento_psicologico = models.TextField(blank=False)
    encaminhamento = models.CharField(blank=False, max_length=255)
    algum_membro_ja_fez_acompanhamento_psicologico = models.TextField(blank=False)
    queixa_psicologica_principal = models.TextField(blank=False)
    
    def __str__(self, ):
        return self.paciente


class Fonoaudiologia(models.Model):
    class Meta:
        verbose_name = "Fonoaudiologia"
        verbose_name_plural = "Fonoaudiologia"

    dt_registro = models.DateTimeField(default=timezone.now, verbose_name='Data')
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    encaminhado = models.TextField(blank=False)
    queixa = models.TextField(blank=False)
    tratamento_anterior = models.TextField(blank=False)
    quando_comecou_sentar = models.TextField(blank=False)
    quando_engatinhou = models.TextField(blank=False)
    quando_andou = models.TextField(blank=False)
    quando_comeu = models.TextField(blank=False)
    quando_balburciou = models.TextField(blank=False)
    primeiras_palavras = models.TextField(blank=False)
    articulacao_palavras = models.TextField(blank=False)
    regressao_linguistica = models.TextField(blank=False)
    comunicacao_atual = models.TextField(blank=False)
    mamadeira_chupeta = models.TextField(blank=False)
    horas_de_sono = models.TextField(blank=False)
    autonomia_dormir = models.TextField(blank=False)
    doencas_alergias = models.TextField(blank=False)
    acompanhamento_medico = models.TextField(blank=False)
    acompanhamento_fonoaudiologico = models.TextField(blank=False)
    exames_fonoaudiologicos = models.TextField(blank=False)
    teste_orelinha = models.TextField(blank=False)
    idade_comecou_escola = models.TextField(blank=False)
    alfabetizado = models.TextField(blank=False)
    materia_mais_gosta = models.TextField(blank=False)
    relacionamento_pais = models.TextField(blank=False)
    relacionamento_criancas = models.TextField(blank=False)
    hobby = models.TextField(blank=False)
    familiar_dificuldades_na_fala = models.TextField(blank=False)
    prende_atencao = models.TextField(blank=False)
    gosta_de_brincar = models.TextField(blank=False)
    compreende_comandos = models.TextField(blank=False)
    contato_visual = models.TextField(blank=False)
    interage = models.TextField(blank=False)
    atencao_por_tempo_significativo = models.TextField(blank=False)
    expectativa_do_acompanhamento_fonoaudiologico = models.TextField(blank=False)

    def __str__(self, ):
        return self.paciente


class Psicomotricidade(models.Model):
    class Meta:
        verbose_name = "Psicomotricidade"
        verbose_name_plural = "Psicomotricidade"

    dt_registro = models.DateTimeField(default=timezone.now, verbose_name='Data')
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    como_era_bebe = models.TextField(blank=False)
    idade_que_firmou_a_cabeca = models.TextField(blank=False)
    sentou_sem_apoio = models.TextField(blank=False)
    engatinhou = models.TextField(blank=False)
    ficou_de_pe = models.TextField(blank=False)
    andou = models.TextField(blank=False)
    fez_uso_do_andaja = models.TextField(blank=False)
    preferecia_pela_mao = models.TextField(blank=False)
    como_realiza_atividades = models.TextField(blank=False)
    anda_bicicleta = models.TextField(blank=False)
    idade_andou_bicicleta = models.TextField(blank=False)
    como_se_sai_nas_brincadeiras = models.TextField(blank=False)
    abotoa_roupas = models.TextField(blank=False)
    troca_roupas_sozinho = models.TextField(blank=False)
    amarra_cadarco = models.TextField(blank=False)
    pega_obj_pequenos = models.TextField(blank=False)
    preferencias_brinquedos = models.TextField(blank=False)
    brincadeiras_sozinho = models.TextField(blank=False)
    outras_preferencias = models.TextField(blank=False)
    nao_gosta = models.TextField(blank=False)
    idade_frequentou_escola = models.TextField(blank=False)
    gosta_escola = models.TextField(blank=False)
    gosta_professores = models.TextField(blank=False)
    relacao_colegas = models.TextField(blank=False)
    dificuldades_no_ambiente_escolar = models.TextField(blank=False)
    atividades_juntos_no_tempo_livre = models.TextField(blank=False)
    pratica_esportes = models.TextField(blank=False)

    def __str__(self, ):
        return self.paciente


class DevolutivaModel(models.Model):
    class Meta:
        verbose_name = "Devolutiva"
        verbose_name_plural = "Devolutiva"

    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    dt_devolutiva = models.DateField(blank=False, verbose_name='Data')
    para = models.CharField(blank=False, max_length=255, verbose_name='Para')
    sintese = models.TextField(blank=False, verbose_name='Síntese')

    def __str__(self, ):
        return self.paciente


class ReunioesExternasModel(models.Model):
    class Meta:
        verbose_name = "Reuniões Externas"
        verbose_name_plural = "Reuniões Externas"

    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    dt_devolutiva = models.DateField(blank=False, verbose_name='Data')
    participantes = models.TextField(blank=False, verbose_name='Participantes')
    sintese = models.TextField(blank=False, verbose_name='Síntese')

    def __str__(self, ):
        return self.paciente


class EncaminhamentoModel(models.Model):
    class Meta:
        verbose_name = "Encaminhamento"
        verbose_name_plural = "Encaminhamento"

    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    dt_devolutiva = models.DateField(blank=False, verbose_name='Data')
    para = models.TextField(blank=False, verbose_name='Participantes')
    sintese = models.TextField(blank=False, verbose_name='Síntese')

    def __str__(self, ):
        return self.paciente


class EvolucaoDiariaModel(models.Model):
    class Meta:
        verbose_name = "Evolução Diária"
        verbose_name_plural = "Evolução Diária"

    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    dt_devolutiva = models.DateField(blank=False, verbose_name='Data')
    sintese = models.TextField(blank=False, verbose_name='Síntese')

    def __str__(self, ):
        return self.paciente

class SupervisaoMultiprofissionalModel(models.Model):
    class Meta:
        verbose_name = "Supervisao Multiprofissional"
        verbose_name_plural = "Supervisao Multiprofissional"

    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    dt_devolutiva = models.DateField(blank=False, verbose_name='Data')
    especialista = models.TextField(blank=False, verbose_name='Especialistas')
    observacao = models.TextField(blank=False, verbose_name='Observações')
    plano_de_acao = models.TextField(blank=False, verbose_name='Plano de Ação')

    def __str__(self, ):
        return self.paciente
    