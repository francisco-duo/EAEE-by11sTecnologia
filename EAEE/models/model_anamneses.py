from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from EAEE.models import model_pacientes, TipoDeVinculoComPacienteModels

ESCOLHA_SIM_NAO = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
)

DESENVOLVIMENTO_MOTOR = (
    ('Coordenação motora fina', 'Coordenação motora fina'),
    ('Coordenação motora global', 'Coordenação motora global'),
    ('Senta em W', 'Senta em W'),
    ('Equilibrio', 'Equilibrio')
)

SENSORIAL = (
    ('Gustativo', 'Gustativo'),
    ('Olfativo', 'Olfativo'),
    ('Tátil', 'Tátil'),
    ('Visual', 'Visual'),
    ('Auditivo', 'Auditivo'),
    ('Vestibular', 'Vestibular'),
    ('Propiocepção', 'Propiocepção')
)

COGNITIVO = (
    ('Reconhece cores', 'Reconhece cores'),
    ('Reconhece números', 'Reconhece números'),
    ('Reconhece formas', 'Reconhece formas'),
    ('Atenção', 'Atenção'),
    ('Concentração', 'Concentração'),
    ('Reciocínio lógico', 'Reciocínio lógico')
)



class Psicopedagogia(models.Model):
    class Meta:
        verbose_name = "Psicopedagogia"
        verbose_name_plural = "Psicopedagogia"

    dt_registro = models.DateTimeField(
        default=timezone.now, verbose_name='Data')
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(
        model_pacientes.PacienteModel, on_delete=models.CASCADE)

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


class Psicologia(models.Model):
    class Meta:
        verbose_name = "Psicologia"
        verbose_name_plural = "Psicologia"

    dt_registro = models.DateTimeField(
        default=timezone.now, verbose_name='Data')
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(
        model_pacientes.PacienteModel, on_delete=models.CASCADE)

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


class Fonoaudiologia(models.Model):
    class Meta:
        verbose_name = "Fonoaudiologia"
        verbose_name_plural = "Fonoaudiologia"

    dt_registro = models.DateTimeField(
        default=timezone.now, verbose_name='Data')
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(
        model_pacientes.PacienteModel, on_delete=models.CASCADE)

    encaminhado = models.TextField(
        blank=True, null=True,
        verbose_name='Encaminhado por'
    )
    queixa = models.TextField(
        blank=True, null=True,
        verbose_name='Queixa'
    )
    tratamento_anterior = models.TextField(
        blank=True, null=True,
        verbose_name='Tratamentos anteriores'
    )
    quando_comecou_sentar = models.TextField(
        blank=True, null=True,
        verbose_name='Quando começou a sentar?'
    )
    quando_engatinhou = models.TextField(
        blank=True, null=True,
        verbose_name='Quando começou a engatinhar?'
    )
    quando_andou = models.TextField(
        blank=True, null=True,
        verbose_name='Quando começou a andar?'
    )
    quando_comeu = models.TextField(
        blank=True, null=True,
        verbose_name='Quando começou a comer?'
    )
    quando_balburciou = models.TextField(
        blank=True, null=True,
        verbose_name='Quando começou a balburciar?'
    )
    primeiras_palavras = models.TextField(
        blank=True, null=True,
        verbose_name='Primeiras palavras'
    )
    articulacao_palavras = models.TextField(
        blank=True, null=True,
        verbose_name='Articula bem?'
    )
    regressao_linguistica = models.TextField(
        blank=True, null=True,
        verbose_name='Houve alguma regressão da linguagem em algum momento?'
    )
    comunicacao_atual = models.TextField(
        blank=True, null=True,
        verbose_name='Como é a comunicação atualmente?'
    )
    mamadeira_chupeta = models.TextField(
        blank=True, null=True,
        verbose_name='Faz uso de mamadeira/ chupeta?'
    )
    horas_de_sono = models.TextField(
        blank=True, null=True,
        verbose_name='Dorme por quantas horas?'
    )
    autonomia_dormir = models.TextField(
        blank=True, null=True,
        verbose_name='Tem autonomia para dormir?'
    )
    doencas_alergias = models.TextField(
        blank=True, null=True,
        verbose_name='Doenças/ alergias?'
    )
    acompanhamento_medico = models.TextField(
        blank=True, null=True,
        verbose_name='Faz algum acompanhamento médico atualmente?'
    )
    acompanhamento_fonoaudiologico = models.TextField(
        blank=True, null=True,
        verbose_name='Faz algum acompanhamento fonoaudiológico'
    )
    exames_fonoaudiologicos = models.TextField(
        blank=True, null=True,
        verbose_name='Já fez exames audiológicos?'
    )
    teste_orelinha = models.TextField(
        blank=True, null=True,
        verbose_name='Já fez teste da orelinha?'
    )
    idade_comecou_escola = models.TextField(
        blank=True, null=True,
        verbose_name='Iniciou a escola com que idade?'
    )
    alfabetizado = models.TextField(
        blank=True, null=True,
        verbose_name='É alfabetizado?'
    )
    materia_mais_gosta = models.TextField(
        blank=True, null=True,
        verbose_name='Matéria que mais gosta?'
    )
    relacionamento_pais = models.TextField(
        blank=True, null=True,
        verbose_name='Como é o relacionamento com os pais?'
    )
    relacionamento_criancas = models.TextField(
        blank=True, null=True,
        verbose_name='Como se relaciona com outras crianças?'
    )
    hobby = models.TextField(
        blank=True, null=True,
        verbose_name='O que gosta de fazer (hobby)?'
    )
    familiar_dificuldades_na_fala = models.TextField(
        blank=True, null=True,
        verbose_name='Alguém na família apresenta/ apresentou dificuldade na fala?'
    )
    prende_atencao = models.TextField(
        blank=True, null=True,
        verbose_name='O que prende a atenção?'
    )
    gosta_de_brincar = models.TextField(
        blank=True, null=True,
        verbose_name='Com o que gosta de brincar?'
    )
    compreende_comandos = models.TextField(
        blank=True, null=True,
        verbose_name='Atende e compreende comandos?'
    )
    contato_visual = models.TextField(
        blank=True, null=True,
        verbose_name='Faz contato visual?'
    )
    interage = models.TextField(
        blank=True, null=True,
        verbose_name='Interage?'
    )
    atencao_por_tempo_significativo = models.TextField(
        blank=True, null=True,
        verbose_name='Mantém a atenção em uma atividade por tempo significativo?'
    )
    expectativa_do_acompanhamento_fonoaudiologico = models.TextField(
        blank=True, null=True,
        verbose_name='Qual a expectativa com o acompanhamento fonoaudiológico?'
    )


class Psicomotricidade(models.Model):
    class Meta:
        verbose_name = "Psicomotricidade"
        verbose_name_plural = "Psicomotricidade"

    dt_registro = models.DateTimeField(
        default=timezone.now, verbose_name='Data')
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(
        model_pacientes.PacienteModel, on_delete=models.CASCADE)

    como_era_bebe = models.TextField(
        blank=True, null=True,
        verbose_name='Como era quando bebê? Calmo ou agitado?'
    )
    idade_que_firmou_a_cabeca = models.TextField(
        blank=True, null=True,
        verbose_name='Em que idade firmou a cabeça?'
    )
    sentou_sem_apoio = models.TextField(
        blank=True, null=True,
        verbose_name='Sentou sem apoio?'
    )
    engatinhou = models.TextField(
        blank=True, null=True,
        verbose_name='Engatinhou?'
    )
    ficou_de_pe = models.TextField(
        blank=True, null=True,
        verbose_name='Ficou de pé?'
    )
    andou = models.TextField(
        blank=True, null=True,
        verbose_name='Andou?'
    )
    fez_uso_do_andaja = models.TextField(
        blank=True, null=True,
        verbose_name='Fez uso do "anda já"? Se sim, por quanto tempo?'
    )
    preferecia_pela_mao = models.TextField(
        blank=True, null=True,
        verbose_name='Preferência por qual das mãos?'
    )
    como_realiza_atividades = models.TextField(
        blank=True, null=True,
        verbose_name='Como realiza as seguintes atividades (pintura, desenho, recorte, colagem, encaixes, quebra-cabeças)?'
    )
    anda_bicicleta = models.TextField(
        blank=True, null=True,
        verbose_name='Sabe andar de bicicleta?'
    )
    idade_andou_bicicleta = models.TextField(
        blank=True, null=True,
        verbose_name='Com que idade aprendeu?'
    )
    como_se_sai_nas_brincadeiras = models.TextField(
        blank=True, null=True,
        verbose_name='Como se sai nas seguintes brincadeiras? (Bola/ Correr/ Corda/ Peteca/ Subir em árvore/ Natação/ Esportes em geral)?'
    )
    abotoa_roupas = models.TextField(
        blank=True, null=True,
        verbose_name='Sabe abotoar e desabotoar roupas?'
    )
    troca_roupas_sozinho = models.TextField(
        blank=True, null=True,
        verbose_name='Troca de roupa sozinho?'
    )
    amarra_cadarco = models.TextField(
        blank=True, null=True,
        verbose_name='Sabe amarrar o cadarço?'
    )
    pega_obj_pequenos = models.TextField(
        blank=True, null=True,
        verbose_name='Conse pegar objetos bem pequenos?'
    )
    preferencias_brinquedos = models.TextField(
        blank=True, null=True,
        verbose_name='Que tipo de brinquedos gosta?'
    )
    brincadeiras_sozinho = models.TextField(
        blank=True, null=True,
        verbose_name='Brincadeiras que pratica sozinho?'
    )
    outras_preferencias = models.TextField(
        blank=True, null=True,
        verbose_name='Outras preferências:'
    )
    nao_gosta = models.TextField(
        blank=True, null=True,
        verbose_name='Do que a criança não gosta?'
    )
    idade_frequentou_escola = models.TextField(
        blank=True, null=True,
        verbose_name='Quando começou a frequentar a escola?'
    )
    gosta_escola = models.TextField(
        blank=True, null=True,
        verbose_name='Gosta de ir à escola?'
    )
    gosta_professores = models.TextField(
        blank=True, null=True,
        verbose_name='Gosta dos professores?'
    )
    relacao_colegas = models.TextField(
        blank=True, null=True,
        verbose_name='Como se relaciona com os colegas da escola?'
    )
    dificuldades_no_ambiente_escolar = models.TextField(
        blank=True, null=True,
        verbose_name='Dificuldades observadas no ambiente escolar?'
    )
    atividades_juntos_no_tempo_livre = models.TextField(
        blank=True, null=True,
        verbose_name='O que fazem juntos no tempo livre?'
    )
    pratica_esportes = models.TextField(
        blank=True, null=True,
        verbose_name='Pratica esportes?'
    )


class TerapiaOcupacional(models.Model):
    class Meta:
        verbose_name = "Terapia Ocupacional"
        verbose_name_plural = "Terapia Ocupacional"

    dt_registro = models.DateTimeField(
        default=timezone.now, verbose_name='Data')
    especialista = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(
        model_pacientes.PacienteModel, on_delete=models.CASCADE,
        verbose_name='Especialista'
    )

    data_nascimento = models.DateTimeField(
        blank=True, null=True, verbose_name='Datas de nascimento'
    )
    escolaridade = models.TextField(
        blank=True, null=True, verbose_name='Escolaridade'
    )
    mae = models.ForeignKey(
        TipoDeVinculoComPacienteModels, blank=True, null=True,
        on_delete=models.DO_NOTHING, verbose_name='Mãe'
    )
    pai = models.ForeignKey(
        TipoDeVinculoComPacienteModels, blank=True, null=True,
        on_delete=models.DO_NOTHING, related_name='terapiaocupacional_pais',
        verbose_name='Pai'
    )
    diagnostico = models.TextField(
        blank=True, null=True, verbose_name='Diagnóstico'
    )
    medicaco = models.TextField(
        blank=True, null=True, verbose_name='Medicação'
    )
    composicao_familiar = models.TextField(
        blank=True, null=True, verbose_name='Composição familiar'
    )
    idade_pregressa_da_gravidez = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='História pregressa da gravidez - idade?'
    )
    planejada_pregressa_da_gravidez = models.CharField(
        blank=True, null=True, choices=ESCOLHA_SIM_NAO, max_length=100,
        verbose_name='História pregressa da gravidez - planejada?'
    )
    pre_natal_pregressa_da_gravidez = models.TextField(
        blank=True, null=True, 
        verbose_name='História pregressa da gravidez - medicamentos?'
    )
    intercorrencias_pregressa_da_gravidez = models.TextField(
        blank=True, null=True,
        verbose_name='História pregressa da gravidez - intercorrências?'
    )
    tipo_de_parto_parto = models.TextField(
        blank=True, null=True,
        verbose_name='Parto - tipo de parto?'
    )
    idade_gestacional = models.TextField(
        blank=True, null=True,
        verbose_name='Parto - idade gestacional?'
    )
    intercorrencias_parto = models.TextField(
        blank=True, null=True,
        verbose_name='Parto - intercorrências?'
    )
    ictericia_periodo_neonatal = models.TextField(
        blank=True, null=True,
        verbose_name='Período Neonatal - ictericia?'
    )
    convulcoes_periodo_neonatal = models.TextField(
        blank=True, null=True,
        verbose_name='Período Neonatal - convulções?'
    )
    amamentacao_periodo_neonatal = models.TextField(
        blank=True, null=True,
        verbose_name='Período Neonatal - amamentação?'
    )
    internacao_periodo_neonatal = models.TextField(
        blank=True, null=True,
        verbose_name='Período Neonatal - internação?'
    )
    controlou_cabeca_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100, choices=ESCOLHA_SIM_NAO,
        verbose_name='Histórico de Desenvolvimento - controlou cabeça?'
    )
    idade_controlou_cabeca_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='Histórico de Desenvolvimento - idade/ meses controlou cabeça?'
    )
    rolou_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100, choices=ESCOLHA_SIM_NAO,
        verbose_name='Histórico de Desenvolvimento - rolou?'
    )
    idade_rolou_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='Histórico de Desenvolvimento - idade/ meses rolou?'
    )
    arrastou_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100, choices=ESCOLHA_SIM_NAO,
        verbose_name='Histórico de Desenvolvimento - arrastou?'
    )
    idade_arrastou_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='Histórico de Desenvolvimento - idade/ meses arrastou?'
    )
    sentou_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100, choices=ESCOLHA_SIM_NAO,
        verbose_name='Histórico de Desenvolvimento - sentou?'
    )
    idade_sentou_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='Histórico de Desenvolvimento - idade/ meses sentou?'
    )
    engatinhou_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100, choices=ESCOLHA_SIM_NAO,
        verbose_name='Histórico de Desenvolvimento - engatinhou?'
    )
    idade_engatinhou_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='Histórico de Desenvolvimento - idade/ meses engatinhou?'
    )
    andou_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='Histórico de Desenvolvimento - andou?'
    )
    idade_andou_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='Histórico de Desenvolvimento - idade/ meses andou?'
    )
    falou_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='Histórico de Desenvolvimento - falou?'
    )
    idade_falou_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='Histórico de Desenvolvimento - idade/ meses falou?'
    )
    controle_esfincter_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='Histórico de Desenvolvimento - controle de esfincter?'
    )
    idade_controle_esfincter_historico_de_desenvolvimento = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='Histórico de Desenvolvimento - idade/ meses controle de esfincter?'
    )
    desenvolimento_motor = models.CharField(
        blank=True, null=True, max_length=100,
        choices=DESENVOLVIMENTO_MOTOR, verbose_name='Desenvolvimento Motor'
    )
    com_quem_e_onde_fica_a_crianca_rotina_da_crianca = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Rotina da criança - Com quem/ onde fica a criança e o que faz durante o dia?'
    )
    relacionamento_familiar_rotina_da_crianca = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Rotina da criança - Relacionamento Familiar?'
    )
    gosta_de_musica_rotina_da_crianca = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Rotina da criança - Gosta de música?'
    )
    hiperfoco_rotina_da_crianca = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Rotina da criança - Hiperfoco?'
    )
    comportamento_rotina_da_crianca = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name='Rotina da criança - Comportamento (humor, birras, medos, tolerância à frustração)?'
    )
    alimentacao_atividades_de_vida_diaria = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='AVD - alimentação?'
    )
    banho_atividades_de_vida_diaria = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='AVD - banho?'
    )
    vesrtir_despir_atividades_de_vida_diaria = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='AVD - vestir/ despir?'
    )
    escovar_dentes_atividades_de_vida_diaria = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='AVD - escovar dentes?'
    )
    uso_do_banheiro_atividades_de_vida_diaria = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name='AVD - uso do banheiro?'
    )
    sensorial_choices = models.CharField(
        blank=True, null=True, max_length=100,
        choices=SENSORIAL, verbose_name='Sensorial'
    )
    sensorial_observacao = models.TextField(
        blank=True, null=True,
        verbose_name='Sensorial - observações'
    )
    seletividade_alimentar_choices = models.CharField(
        blank=True, null=True, max_length=10, choices=ESCOLHA_SIM_NAO,
        verbose_name='Seletividade alimentar?'
    )
    seletividade_alimentar_observacao = models.TextField(
        blank=True, null=True,
        verbose_name='Seletividade alimentar?'
    )
    cognitivo_choices = models.CharField(
        blank=True, null=True, max_length=100, choices=COGNITIVO,
        verbose_name='Cognitivo'
    )
    cognitivo_observacao = models.TextField(
        blank=True, null=True,
        verbose_name='Cognitivo observações'
    )
    principais_demandas = models.TextField(
        blank=True, null=True,
        verbose_name='Principais demandas/ queixas e expectativas com a terapia'
    )
