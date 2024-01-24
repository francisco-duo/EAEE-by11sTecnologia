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

    idade_que_comecou_a_frequentar_escola = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Com que idade começou a frequentar a escola?'
    )
    como_foi_adaptacao = models.TextField(
        blank=True, null=True,
        verbose_name='Como foi a adaptação?'
    )
    reprovou = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Reprovou? Qual Série?'
    )
    ralacao_professores_colegas = models.TextField(
        blank=True, null=True,
        verbose_name='Como se relaciona com os colegas e professores?'
    )
    motivado_escola = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Se sente motivado a ir para escola? Sim ou Não?'
    )
    falta_assiduo = models.TextField(
        blank=True, null=True,
        verbose_name='Assíduo ou falta com frequência?'
    )
    realiza_atividades_com_satisfacao = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Realiza as atividades de casa com satisfação? Sim ou Não?'
    )
    precisa_ajuda = models.TextField(
        blank=True, null=True,
        verbose_name='Precisa de suporte ou é independente ao realizar?'
    )
    predilecao_matematica_portugues = models.TextField(
        blank=True, null=True,
        verbose_name='Demonstra predileção por matemática ou língua portuguesa?'
    )
    dificuldades_aprendizagem = models.TextField(
        blank=True, null=True,
        verbose_name='Que dificuldades de aprendizagem você observa?'
    )
    antecedentes_com_dificuldade = models.TextField(
        blank=True, null=True,
        verbose_name='Na família, há antecedentes com dificuldade?'
    )
    queixas_comuns_escola = models.TextField(
        blank=True, null=True,
        verbose_name='Queixas comuns da escola?'
    )
    fala_compreensivel = models.TextField(
        blank=True, null=True,
        verbose_name='Fala comppreensível? Observa troca ou omissões de fonemas? Conta uma história com começo, meio e fim?'
    )
    # troca_ou_omissao_fonemas = models.TextField(blank=True, null=True)
    # conta_historia = models.TextField(blank=True, null=True)
    corporalmente_desenvolto = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='É corporalmente desenvolto?'
    )
    anda_bicicleta = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Anda de bicicleta, patins, patinete...?'
    )
    organizado = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Organizado com seus pertences? Sim ou Não?'
    )
    ajuda_em_casa = models.TextField(
        blank=True, null=True,
        verbose_name='Ajuda na organização da casa? Que afazeres são de sua responsabilidade?'
    )
    censurado = models.TextField(
        blank=True, null=True,
        verbose_name='É muito censurado?'
    )
    brinquedos_favorito = models.TextField(
        blank=True, null=True,
        verbose_name='Brinquedos/Brincadeiras/Personagens/Programas de TV favoritos'
    )
    gosta_desenhar = models.TextField(
        blank=True, null=True,
        verbose_name='Gosta de desenhar, colorir, modelar?'
    )
    uso_de_eletronicos = models.TextField(
        blank=True, null=True,
        verbose_name='Tempo diário de uso em eletrônicos (celulares, tablets e afins)'
    )
    horas_livres = models.TextField(
        blank=True, null=True,
        verbose_name='O que gosta de fazer nas horas livres?'
    )
    potencialidades_marcantes = models.TextField(
        blank=True, null=True,
        verbose_name='Potencialidades marcantes?'
    )
    fragilidades_evidentes = models.TextField(
        blank=True, null=True,
        verbose_name='Fragilidades evidentes'
    )

    def __str__(self, ):
        return self.paciente


class Psicologia(models.Model):
    class Meta:
        verbose_name = "Psicologia"
        verbose_name_plural = "Psicologia"

    dt_registro = models.DateTimeField(default=timezone.now, verbose_name='Data')
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(model_pacientes.PacienteModel, on_delete=models.CASCADE)

    numero_irmaos = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Número de irmãos'
    )
    reacao_nascimento_irmao = models.TextField(
        blank=True, null=True,
        verbose_name='Reação da criança em relação ao nascimento de irmãos mais novos'
    )
    relacionamento_irmaos = models.TextField(
        blank=True, null=True,
        verbose_name='Relacionamento com os irmãos'
    )
    relacionamento_pais = models.TextField(
        blank=True, null=True,
        verbose_name='Relacionamento com os pais'
    )
    relacionamento_familia = models.TextField(
        blank=True, null=True,
        verbose_name='Relacionamento com a família materna e paterna'
    )
    personalidade = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Personalidade'
    )
    comportamento_roer_unhas = models.TextField(
        blank=True, null=True,
        verbose_name='Comportamento de roer unhas/ Chupar dedos/ Tique'
    )
    humor_habitual = models.TextField(
        blank=True, null=True,
        verbose_name='Humor habitual'
    )
    brinca_sozinho_ou_grupo = models.TextField(
        blank=True, null=True,
        verbose_name='Prefere brincar sozinho ou em grupo?'
    )
    estranha_mudancas_ambiente = models.TextField(
        blank=True, null=True,
        verbose_name='Estranha mudanças no ambiente?'
    ) 
    aceita_seguir_comandos = models.TextField(
        blank=True, null=True,
        verbose_name='Aceita seguir comandos?'
    )
    brincadeiras_brinquedo_favorito = models.TextField(
        blank=True, null=True,
        verbose_name='Brinquedos e brincadeiras preferidas?'
    )
    gosta_de_musicas = models.TextField(
        blank=True, null=True,
        verbose_name='Gosta de música? Quais'
    )
    baste_cabeca_na_parede = models.TextField(
        blank=True, null=True,
        verbose_name='Bate a cabeça na parede?'
    )
    atitudes_desse_habito = models.TextField(
        blank=True, null=True,
        verbose_name='Que atitudes são tomadas diante desse hábito'
    )
    reprovou_na_escola = models.TextField(
        blank=True, null=True,
        verbose_name='Reprovou na escola?'
    )
    relacionamento_colegas = models.TextField(
        blank=True, null=True,
        verbose_name='Relacionamento com os colegas das escola?'
    )
    relacionamento_professores = models.TextField(
        blank=True, null=True,
        verbose_name='Relacionamento com os professores da escola?'
    )
    idade_desfralde = models.TextField(
        blank=True, null=True,
        verbose_name='Com que idade ocorreu o desfraude?'
    )
    dificuldades_desfraude = models.TextField(
        blank=True, null=True,
        verbose_name='Apresentou dificuldades? Se sim, qual a posição dos pais?'
    )
    higiene_sozinho = models.TextField(
        blank=True, null=True,
        verbose_name='Faz higiene sozinho?'
    )
    idade_higiene_sozinho = models.TextField(
        blank=True, null=True,
        verbose_name='Se sim, começou com que idade?'
    )
    problema_na_fala = models.TextField(
        blank=True, null=True,
        verbose_name='Apresenta alguma problemma ao falar?'
    )
    troca_letras = models.TextField(
        blank=True, null=True,
        verbose_name='Troca letras?'
    )
    acorda_vai_para_cama_dos_pais = models.TextField(
        blank=True, null=True,
        verbose_name='Quando acorda vai para a cama dos pais?'
    )
    dorme_sozinho = models.TextField(
        blank=True, null=True,
        verbose_name='Medo de dormir sozinho?'
    )
    objeto_para_dormir = models.TextField(
        blank=True, null=True,
        verbose_name='Utiliza algum objeto para dormir?'
    )
    urina_na_cama = models.TextField(
        blank=True, null=True,
        verbose_name='Costuma urinar na cama?'
    )
    horario_para_refeicoes = models.TextField(
        blank=True, null=True,
        verbose_name='Tem horário para as refeições?'
    )
    refeicoes_em_familia = models.TextField(
        blank=True, null=True,
        verbose_name='Faz as refeições com a família?'
    )
    local = models.TextField(
        blank=True, null=True,
        verbose_name='Em que local?'
    )
    assiste_enquanto_come = models.TextField(
        blank=True, null=True,
        verbose_name='Enquanto come, assiste a TV ou mexe em eletrônicos?'
    )
    como_se_alimenta = models.TextField(
        blank=True, null=True,
        verbose_name='Como se alimenta (rápido, devagar, mastiga bem, ...)?'
    )
    seletividade_alimentar = models.TextField(
        blank=True, null=True,
        verbose_name='Apresenta seletividade alimentar?'
    )
    curiosidade_sexual = models.TextField(
        blank=True, null=True,
        verbose_name='Apresentou curiosidade sexual?'
    )
    atitude_dos_pais = models.TextField(
        blank=True, null=True,
        verbose_name='Qual a atitude dos pais?'
    )
    informacoes_sexuais = models.TextField(
        blank=True, null=True,
        verbose_name='Acha importante das informações sexuais? Por que?'
    )
    tratamento_medico = models.TextField(
        blank=True, null=True,
        verbose_name='Faz algum tratamento médico'
    )
    internado = models.TextField(
        blank=True, null=True,
        verbose_name='Já esteve internado?'
    )
    motivo_internação = models.TextField(
        blank=True, null=True,
        verbose_name='Motivo da internação?'
    )
    operado = models.TextField(
        blank=True, null=True,
        verbose_name='Ja foi operado?'
    )
    idade_operado = models.TextField(
        blank=True, null=True,
        verbose_name='Com que idade?'
    )
    adoece_facilmente = models.TextField(
        blank=True, null=True,
        verbose_name='Adoece facilente?'
    )
    acompanhamento_psicologico = models.TextField(
        blank=True, null=True,
        verbose_name='Fez acompanhamento psicológico antes?'
    )
    encaminhamento = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Encaminhamento?'
    )
    algum_membro_ja_fez_acompanhamento_psicologico = models.TextField(
        blank=True, null=True,
        verbose_name='Algum membro da família faz ou fez acompanhamento psicológico?'
    )
    queixa_psicologica_principal = models.TextField(
        blank=True, null=True,
        verbose_name='Queixa psicológica principal'
    )

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
