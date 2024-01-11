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
    idade_que_comecou_a_frequentar_escola = models.CharField(blank=True, null=True, max_length=255)
    como_foi_adaptacao = models.TextField(blank=True, null=True)
    reprovou = models.CharField(blank=True, null=True, max_length=255)
    ralacao_professores_colegas = models.TextField(blank=True, null=True)
    motivado_escola = models.CharField(blank=True, null=True, max_length=255)
    falta_assiduo = models.TextField(blank=True, null=True)
    realiza_atividades_com_satisfacao = models.CharField(blank=True, null=True, max_length=255)
    precisa_ajuda = models.TextField(blank=True, null=True)
    predilecao_matematica_portugues = models.TextField(blank=True, null=True)
    dificuldades_aprendizagem = models.TextField(blank=True, null=True)
    antecedentes_com_dificuldade = models.TextField(blank=True, null=True)
    queixas_comuns_escola = models.TextField(blank=True, null=True)
    fala_compreensivel = models.TextField(blank=True, null=True)
    # troca_ou_omissao_fonemas = models.TextField(blank=True, null=True)
    # conta_historia = models.TextField(blank=True, null=True)
    corporalmente_desenvolto = models.CharField(blank=True, null=True, max_length=255)
    anda_bicicleta = models.CharField(blank=True, null=True, max_length=255)
    organizado = models.CharField(blank=True, null=True, max_length=255)
    ajuda_em_casa = models.TextField(blank=True, null=True)
    censurado = models.TextField(blank=True, null=True)
    brinquedos_favorito = models.TextField(blank=True, null=True)
    gosta_desenhar = models.TextField(blank=True, null=True)
    uso_de_eletronicos = models.TextField(blank=True, null=True)
    horas_livres = models.TextField(blank=True, null=True)
    potencialidades_marcantes = models.TextField(blank=True, null=True)
    fragilidades_evidentes = models.TextField(blank=True, null=True)

    def __str__(self, ):
        return self.paciente


class Psicologia(models.Model):
    class Meta:
        verbose_name = "Psicologia"
        verbose_name_plural = "Psicologia"
    dt_registro = models.DateTimeField(default=timezone.now, verbose_name='Data')
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    numero_irmaos = models.CharField(blank=True, null=True, max_length=255)
    reacao_nascimento_irmao = models.TextField(blank=True, null=True)
    relacionamento_irmaos = models.TextField(blank=True, null=True)
    relacionamento_pais = models.TextField(blank=True, null=True)
    relacionamento_familia = models.TextField(blank=True, null=True)
    personalidade = models.CharField(blank=True, null=True, max_length=255)
    comportamento_roer_unhas = models.TextField(blank=True, null=True)
    humor_habitual = models.TextField(blank=True, null=True)
    brinca_sozinho_ou_grupo = models.TextField(blank=True, null=True)
    estranha_mudancas_ambiente = models.TextField(blank=True, null=True) 
    aceita_seguir_comandos = models.TextField(blank=True, null=True)
    brincadeiras_brinquedo_favorito = models.TextField(blank=True, null=True)
    gosta_de_musicas = models.TextField(blank=True, null=True)
    baste_cabeca_na_parede = models.TextField(blank=True, null=True)
    atitudes_desse_habito = models.TextField(blank=True, null=True)
    reprovou_na_escola = models.TextField(blank=True, null=True)
    relacionamento_colegas = models.TextField(blank=True, null=True)
    relacionamento_professores = models.TextField(blank=True, null=True)
    idade_desfralde = models.TextField(blank=True, null=True)
    dificuldades_desfraude = models.TextField(blank=True, null=True)
    higiene_sozinho = models.TextField(blank=True, null=True)
    idade_higiene_sozinho = models.TextField(blank=True, null=True)
    problema_na_fala = models.TextField(blank=True, null=True)
    troca_letras = models.TextField(blank=True, null=True)
    acorda_vai_para_cama_dos_pais = models.TextField(blank=True, null=True)
    dorme_sozinho = models.TextField(blank=True, null=True)
    objeto_para_dormir = models.TextField(blank=True, null=True)
    urina_na_cama = models.TextField(blank=True, null=True)
    horario_para_refeicoes = models.TextField(blank=True, null=True)
    refeicoes_em_familia = models.TextField(blank=True, null=True)
    local = models.TextField(blank=True, null=True)
    assiste_enquanto_come = models.TextField(blank=True, null=True)
    como_se_alimenta = models.TextField(blank=True, null=True)
    seletividade_alimentar = models.TextField(blank=True, null=True)
    curiosidade_sexual = models.TextField(blank=True, null=True)
    atitude_dos_pais = models.TextField(blank=True, null=True)
    informacoes_sexuais = models.TextField(blank=True, null=True)
    tratamento_medico = models.TextField(blank=True, null=True)
    internado = models.TextField(blank=True, null=True)
    motivo_internação = models.TextField(blank=True, null=True)
    operado = models.TextField(blank=True, null=True)
    idade_operado = models.TextField(blank=True, null=True)
    adoece_facilmente = models.TextField(blank=True, null=True)
    acompanhamento_psicologico = models.TextField(blank=True, null=True)
    encaminhamento = models.CharField(blank=True, null=True, max_length=255)
    algum_membro_ja_fez_acompanhamento_psicologico = models.TextField(blank=True, null=True)
    queixa_psicologica_principal = models.TextField(blank=True, null=True)

    def __str__(self, ):
        return self.paciente


class Fonoaudiologia(models.Model):
    class Meta:
        verbose_name = "Fonoaudiologia"
        verbose_name_plural = "Fonoaudiologia"

    dt_registro = models.DateTimeField(default=timezone.now, verbose_name='Data')
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    encaminhado = models.TextField(blank=True, null=True)
    queixa = models.TextField(blank=True, null=True)
    tratamento_anterior = models.TextField(blank=True, null=True)
    quando_comecou_sentar = models.TextField(blank=True, null=True)
    quando_engatinhou = models.TextField(blank=True, null=True)
    quando_andou = models.TextField(blank=True, null=True)
    quando_comeu = models.TextField(blank=True, null=True)
    quando_balburciou = models.TextField(blank=True, null=True)
    primeiras_palavras = models.TextField(blank=True, null=True)
    articulacao_palavras = models.TextField(blank=True, null=True)
    regressao_linguistica = models.TextField(blank=True, null=True)
    comunicacao_atual = models.TextField(blank=True, null=True)
    mamadeira_chupeta = models.TextField(blank=True, null=True)
    horas_de_sono = models.TextField(blank=True, null=True)
    autonomia_dormir = models.TextField(blank=True, null=True)
    doencas_alergias = models.TextField(blank=True, null=True)
    acompanhamento_medico = models.TextField(blank=True, null=True)
    acompanhamento_fonoaudiologico = models.TextField(blank=True, null=True)
    exames_fonoaudiologicos = models.TextField(blank=True, null=True)
    teste_orelinha = models.TextField(blank=True, null=True)
    idade_comecou_escola = models.TextField(blank=True, null=True)
    alfabetizado = models.TextField(blank=True, null=True)
    materia_mais_gosta = models.TextField(blank=True, null=True)
    relacionamento_pais = models.TextField(blank=True, null=True)
    relacionamento_criancas = models.TextField(blank=True, null=True)
    hobby = models.TextField(blank=True, null=True)
    familiar_dificuldades_na_fala = models.TextField(blank=True, null=True)
    prende_atencao = models.TextField(blank=True, null=True)
    gosta_de_brincar = models.TextField(blank=True, null=True)
    compreende_comandos = models.TextField(blank=True, null=True)
    contato_visual = models.TextField(blank=True, null=True)
    interage = models.TextField(blank=True, null=True)
    atencao_por_tempo_significativo = models.TextField(blank=True, null=True)
    expectativa_do_acompanhamento_fonoaudiologico = models.TextField(blank=True, null=True)

    def __str__(self, ):
        return self.paciente


class Psicomotricidade(models.Model):
    class Meta:
        verbose_name = "Psicomotricidade"
        verbose_name_plural = "Psicomotricidade"

    dt_registro = models.DateTimeField(default=timezone.now, verbose_name='Data')
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)
    como_era_bebe = models.TextField(blank=True, null=True)
    idade_que_firmou_a_cabeca = models.TextField(blank=True, null=True)
    sentou_sem_apoio = models.TextField(blank=True, null=True)
    engatinhou = models.TextField(blank=True, null=True)
    ficou_de_pe = models.TextField(blank=True, null=True)
    andou = models.TextField(blank=True, null=True)
    fez_uso_do_andaja = models.TextField(blank=True, null=True)
    preferecia_pela_mao = models.TextField(blank=True, null=True)
    como_realiza_atividades = models.TextField(blank=True, null=True)
    anda_bicicleta = models.TextField(blank=True, null=True)
    idade_andou_bicicleta = models.TextField(blank=True, null=True)
    como_se_sai_nas_brincadeiras = models.TextField(blank=True, null=True)
    abotoa_roupas = models.TextField(blank=True, null=True)
    troca_roupas_sozinho = models.TextField(blank=True, null=True)
    amarra_cadarco = models.TextField(blank=True, null=True)
    pega_obj_pequenos = models.TextField(blank=True, null=True)
    preferencias_brinquedos = models.TextField(blank=True, null=True)
    brincadeiras_sozinho = models.TextField(blank=True, null=True)
    outras_preferencias = models.TextField(blank=True, null=True)
    nao_gosta = models.TextField(blank=True, null=True)
    idade_frequentou_escola = models.TextField(blank=True, null=True)
    gosta_escola = models.TextField(blank=True, null=True)
    gosta_professores = models.TextField(blank=True, null=True)
    relacao_colegas = models.TextField(blank=True, null=True)
    dificuldades_no_ambiente_escolar = models.TextField(blank=True, null=True)
    atividades_juntos_no_tempo_livre = models.TextField(blank=True, null=True)
    pratica_esportes = models.TextField(blank=True, null=True)

    def __str__(self, ):
        return self.paciente
