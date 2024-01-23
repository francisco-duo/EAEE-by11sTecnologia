from django.http import Http404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from EAEE.forms import (
    PacienteForm, ResponsavelForm, InformacoesComplementaresForm,
    DevolutivaForm
)
from EAEE.models import *


def teste(request, ):
    return redirect('login')


def cadastrar_novo_paciente(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PacienteForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                return redirect('cadastrar_paciente', request.user.username)
        return render(
            request, 'pages/pacientes/cadastro_paciente.html',
            {'form': PacienteForm()}
        )
    else:
        return redirect('login')


def cadastrar_responsavel(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ResponsavelForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

            return redirect('inicio', usuario=request.user.username)
        return render(
            request, 'pages/pacientes/cadastro_responsavel.html',
            {'form': ResponsavelForm()}
        )
    else:
        return redirect('login')


def paciente_inforacoes_complementares(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = InformacoesComplementaresForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                return redirect(
                    'inicio', request.user.username
                )

        return render(
            request, 'pages/pacientes/cadastrar_informacoes_complementares.html',
            {'form': InformacoesComplementaresForm}
        )
    else:
        return redirect('login')


def anamnese_psicopedagogia(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Psicopedagogia.objects.create(
                especialista=request.user,
                paciente=PacienteModel.objects.get(
                    id=request.POST.get('paciente')),
                idade_que_comecou_a_frequentar_escola=request.POST.get(
                    'idade_que_frequentou_a_escola'),
                como_foi_adaptacao=request.POST.get('como_foi_a_adaptacao'),
                reprovou=request.POST.get('reprovou_qual_serie'),
                ralacao_professores_colegas=request.POST.get(
                    'como_se_relaciona_com_os_colegas_e_professores'),
                motivado_escola=request.POST.get('motiva_a_ir_para_escola'),
                falta_assiduo=request.POST.get('assiduo_com_frequencia'),
                realiza_atividades_com_satisfacao=request.POST.get(
                    'realiza_atividades_com_frequencia'),
                precisa_ajuda=request.POST.get('independente'),
                predilecao_matematica_portugues=request.POST.get(
                    'matematica_ou_portugues'),
                dificuldades_aprendizagem=request.POST.get(
                    'dificuldade_de_aprendizagem'),
                antecedentes_com_dificuldade=request.POST.get('antecedentes'),
                queixas_comuns_escola=request.POST.get('queixas'),
                fala_compreensivel=request.POST.get('compreensivel'),
                # troca_ou_omissao_fonemas=request.POST.get('corpo_desenvolto'),
                # conta_historia=request.POST.get('bicicleta'),
                corporalmente_desenvolto=request.POST.get('corpo_desenvolto'),
                anda_bicicleta=request.POST.get('bicicleta'),
                organizado=request.POST.get('organizado'),
                ajuda_em_casa=request.POST.get('ajuda'),
                censurado=request.POST.get('censura'),
                brinquedos_favorito=request.POST.get('brinquedos'),
                gosta_desenhar=request.POST.get('desenhar'),
                uso_de_eletronicos=request.POST.get('tempo_eletronico'),
                horas_livres=request.POST.get('hora_livre'),
                potencialidades_marcantes=request.POST.get('potencialidades'),
                fragilidades_evidentes=request.POST.get('fragilidades'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/anamnese_psicopedagogia.html', {'pacientes': PacienteModel.objects.all().order_by('-id')})
    else:
        return redirect('login')


def anamnese_psicologia(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Psicologia.objects.create(
                especialista=request.user,
                paciente=PacienteModel.objects.get(
                    id=request.POST.get('paciente')),
                numero_irmaos=request.POST.get('qnt_irmaos'),
                reacao_nascimento_irmao=request.POST.get('reacao_nascimento'),
                relacionamento_irmaos=request.POST.get(
                    'relacionamento_irmaos'),
                relacionamento_pais=request.POST.get('relacionamento_pais'),
                relacionamento_familia=request.POST.get(
                    'relacionamento_familia'),
                personalidade=request.POST.get('personalidade'),
                comportamento_roer_unhas=request.POST.get('comportamento'),
                humor_habitual=request.POST.get('humor'),
                brinca_sozinho_ou_grupo=request.POST.get('brincar_sozinho'),
                estranha_mudancas_ambiente=request.POST.get('mudanca_humor'),
                aceita_seguir_comandos=request.POST.get('seguir_comandos'),
                brincadeiras_brinquedo_favorito=request.POST.get(
                    'brincadeiras'),
                gosta_de_musicas=request.POST.get('gosta_musica'),
                baste_cabeca_na_parede=request.POST.get('bate_parede'),
                atitudes_desse_habito=request.POST.get('habito'),
                reprovou_na_escola=request.POST.get('reprovou'),
                relacionamento_colegas=request.POST.get(
                    'relacionamento_escola'),
                relacionamento_professores=request.POST.get(
                    'relacionamento_professores'),
                idade_desfralde=request.POST.get('idade_desfraude'),
                dificuldades_desfraude=request.POST.get(
                    'desfraude_dificuldades'),
                higiene_sozinho=request.POST.get('higiene'),
                idade_higiene_sozinho=request.POST.get('banho'),
                problema_na_fala=request.POST.get('problema_fala'),
                troca_letras=request.POST.get('troca_letras'),
                acorda_vai_para_cama_dos_pais=request.POST.get(
                    'cama_dos_pais'),
                dorme_sozinho=request.POST.get('medo_dormir_sozinho'),
                objeto_para_dormir=request.POST.get('objeto_para_dormir'),
                urina_na_cama=request.POST.get('urina_na_cama'),
                horario_para_refeicoes=request.POST.get('horario_refeicoes'),
                refeicoes_em_familia=request.POST.get('refeicoes_familia'),
                local=request.POST.get('local'),
                assiste_enquanto_come=request.POST.get('assite_enquanto_come'),
                como_se_alimenta=request.POST.get('como_se_alimenta'),
                seletividade_alimentar=request.POST.get(
                    'seletividade_alimentar'),
                curiosidade_sexual=request.POST.get('curiosidade_sexual'),
                atitude_dos_pais=request.POST.get('atitude dos pais'),
                informacoes_sexuais=request.POST.get('informacoes_ sexuais'),
                tratamento_medico=request.POST.get('tratamento_medico'),
                internado=request.POST.get('esteve_internado'),
                motivo_internação=request.POST.get('motivo_internacao'),
                operado=request.POST.get('foi_operado'),
                idade_operado=request.POST.get('idade_operado'),
                adoece_facilmente=request.POST.get('adoece'),
                acompanhamento_psicologico=request.POST.get(
                    'faz_acompanhamento'),
                encaminhamento=request.POST.get('encaminhamento'),
                algum_membro_ja_fez_acompanhamento_psicologico=request.POST.get(
                    'membro_acompanhamento'),
                queixa_psicologica_principal=request.POST.get('queixa'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/anamnese_psicologia.html', {'pacientes': PacienteModel.objects.all().order_by('-id')})
    else:
        return redirect('login')


def anamnese_fonoaudiologia(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Fonoaudiologia.objects.create(
                especialista=User.objects.get(id=request.user.id),
                paciente=PacienteModel.objects.get(
                    id=request.POST.get('paciente')),
                encaminhado=request.POST.get('Encaminhado por'),
                queixa=request.POST.get('Queixa'),
                tratamento_anterior=request.POST.get('Tratamentos anteriores'),
                quando_comecou_sentar=request.POST.get(
                    'Quando começou a sentar'),
                quando_engatinhou=request.POST.get(
                    'Quando começou a engatinhar'),
                quando_andou=request.POST.get('Quando começou a andar'),
                quando_comeu=request.POST.get('Quando começou a comer'),
                quando_balburciou=request.POST.get(
                    'Quando começou a balbuciar?'),
                primeiras_palavras=request.POST.get('Primeiras palavras'),
                articulacao_palavras=request.POST.get('Articula bem'),
                regressao_linguistica=request.POST.get(
                    'Houve alguma regressão da linguagem em algum momento'),
                comunicacao_atual=request.POST.get(
                    'Como é a comunicação atualmente'),
                mamadeira_chupeta=request.POST.get(
                    'Como é a comunicação atualmente'),
                horas_de_sono=request.POST.get('Dorme por quantas horas?'),
                autonomia_dormir=request.POST.get(
                    'Tem autonomia para dormir?'),
                doencas_alergias=request.POST.get('Doenças / alergias?'),
                acompanhamento_medico=request.POST.get(
                    'Faz algum acompanhamento médico atualmente?'),
                acompanhamento_fonoaudiologico=request.POST.get(
                    'Já fez acompanhamento fonoaudiológico? Quando?'),
                exames_fonoaudiologicos=request.POST.get(
                    'Já fez exames audiológicos?'),
                teste_orelinha=request.POST.get('Já fez teste da orelhinha?'),
                idade_comecou_escola=request.POST.get(
                    'Iniciou com que idade?'),
                alfabetizado=request.POST.get('Alfabetizado?'),
                materia_mais_gosta=request.POST.get('Matéria que mais gosta?'),
                relacionamento_pais=request.POST.get(
                    'Como é o relacionamento com os pais?'),
                relacionamento_criancas=request.POST.get(
                    'Como se relaciona com outras crianças?'),
                hobby=request.POST.get('O que gosta de fazer (hobby)?'),
                familiar_dificuldades_na_fala=request.POST.get(
                    'Alguém na família apresenta/ apresentou dificuldade na fala?'),
                prende_atencao=request.POST.get('O que prende a atenção?'),
                gosta_de_brincar=request.POST.get(
                    'Com o que gosta de brincar?'),
                compreende_comandos=request.POST.get(
                    'Atende e compreende comandos?'),
                contato_visual=request.POST.get('Faz contato visual?'),
                interage=request.POST.get('Interage?'),
                atencao_por_tempo_significativo=request.POST.get(
                    'Mantém a atenção em uma atividade por um tempo significativo?'),
                expectativa_do_acompanhamento_fonoaudiologico=request.POST.get(
                    'Qual a expectativa com o acompanhamento fonoaudiológico?'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/anamnese_fonoaudiologia.html', {'pacientes': PacienteModel.objects.all().order_by('-id')})
    else:
        return redirect('login')


def anamnese_psicomotricidade(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Psicomotricidade.objects.create(
                especialista=request.user,
                paciente=PacienteModel.objects.get(
                    id=request.POST.get('paciente')),
                como_era_bebe=request.POST.get(
                    'Como era quando bebê? Calmo ou agitado?'),
                idade_que_firmou_a_cabeca=request.POST.get(
                    'Em que idade firmou a cabeça?'),
                sentou_sem_apoio=request.POST.get('Sentou sem apoio?'),
                engatinhou=request.POST.get('Engatinhou?'),
                ficou_de_pe=request.POST.get('Ficou de pé?'),
                andou=request.POST.get('Quando começou a andar'),
                fez_uso_do_andaja=request.POST.get(
                    'Fez uso do “anda já”? Se sim, por quanto tempo?'),
                preferecia_pela_mao=request.POST.get(
                    'Preferência por qual das mãos?'),
                como_realiza_atividades=request.POST.get(
                    'Como realiza as seguintes atividades (pintura, desenho, recorte, colagem, encaixes, quebra-cabeça)?'),
                anda_bicicleta=request.POST.get('Sabe andar de bicicleta?'),
                idade_andou_bicicleta=request.POST.get(
                    'Com que idade aprendeu?'),
                como_se_sai_nas_brincadeiras=request.POST.get(
                    'Como se sai nas seguintes brincadeiras/ atividades:'),
                abotoa_roupas=request.POST.get(
                    'Sabe abotoar e desabotoar roupas?'),
                troca_roupas_sozinho=request.POST.get(
                    'Troca de roupa sozinho?'),
                amarra_cadarco=request.POST.get('Sabe amarrar o cadarço?'),
                pega_obj_pequenos=request.POST.get(
                    'Consegue pega objetos bem pequenos?'),
                preferencias_brinquedos=request.POST.get(
                    'Que tipo de brinquedos gosta?'),
                brincadeiras_sozinho=request.POST.get(
                    'Brincadeiras que pratica sozinho?'),
                outras_preferencias=request.POST.get('Outras preferências:'),
                nao_gosta=request.POST.get('Do que a criança não gosta?'),
                idade_frequentou_escola=request.POST.get(
                    'Quando começou a frequentar a escola?'),
                gosta_escola=request.POST.get('Gosta de ir à escola?'),
                gosta_professores=request.POST.get('Gosta dos professores?'),
                relacao_colegas=request.POST.get(
                    'Como se relaciona com os colegas da escola?'),
                dificuldades_no_ambiente_escolar=request.POST.get(
                    'Dificuldades observadas no ambiente escolar:'),
                atividades_juntos_no_tempo_livre=request.POST.get(
                    'O que fazem juntos no tempo livre?'),
                pratica_esportes=request.POST.get('Pratica esportes?'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/anamnese_psicomotricidade.html', {'pacientes': PacienteModel.objects.all().order_by('-id')})
    else:
        return redirect('login')


def devolutiva(request, usuario):
    if request.user.is_authenticated:
        form = DevolutivaForm()
        if request.method == 'POST':
            form = DevolutivaForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('devolutiva', request.user.username)
        if request.method == 'POST':

            return redirect('inicio', usuario=request.user.username)
        return render(
            request, 'pages/devolutiva.html',
            {'form': form}
        )
    else:
        return redirect('login')


def devolutivas(request, usuario):
    if request.user.is_authenticated:
        pacientes = Devolutiva.objects.all().order_by('-id')
        paginator = Paginator(pacientes, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'pages/devolutivas.html', {'page_obj': page_obj})
    else:
        return redirect('login') 


def devolutiva_visualizar(request, usuario, pk):
    if request.user.is_authenticated:
        try:
            paciente = Devolutiva.objects.get(id=pk)
            paciente_form = DevolutivaForm(instance=paciente)

        except PacienteModel.DoesNotExist:
            raise Http404('Devolutiva não encontrado')

        if request.method == 'POST':
            paciente_form.save()

        return render(request, 'pages/devolutiva_visualizar.html', {'paciente_form': paciente_form})
    else:
        return redirect('login')


def reunioes_externas(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ReunioesExternasModel.objects.create(
                paciente=PacienteModel.objects.get(
                    id=request.POST.get('paciente')),
                dt_devolutiva=request.POST.get('data'),
                participantes=request.POST.get('participantes envolvidos'),
                sintese=request.POST.get('sintese'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/reunioes_externas.html', {'pacientes': PacienteModel.objects.all().order_by('-id')})
    else:
        return redirect('login')


def encaminhamento(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            EncaminhamentoModel.objects.create(
                paciente=PacienteModel.objects.get(
                    id=request.POST.get('paciente')),
                dt_devolutiva=request.POST.get('data'),
                para=request.POST.get('para'),
                sintese=request.POST.get('sintese'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/encaminhamento.html', {'pacientes': PacienteModel.objects.all().order_by('-id')})
    else:
        return redirect('login')


def evolucao_diaria(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            EvolucaoDiariaModel.objects.create(
                paciente=PacienteModel.objects.get(
                    id=request.POST.get('paciente')),
                dt_devolutiva=request.POST.get('patient-name'),
                sintese=request.POST.get('vinculo'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/evolucao_diaria.html', {'pacientes': PacienteModel.objects.all().order_by('-id')})
    else:
        return redirect('login')


def supervisao_multiprofissional(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            SupervisaoMultiprofissionalModel.objects.create(
                paciente=PacienteModel.objects.get(
                    id=request.POST.get('paciente')),
                dt_devolutiva=request.POST.get('data'),
                especialista=request.POST.get('especialista envolvido'),
                observacao=request.POST.get('observacoes  coletivas'),
                plano_de_acao=request.POST.get('plano de acao'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/supervisao_multiprofissional.html', {'pacientes': PacienteModel.objects.all().order_by('-id')})
    else:
        return redirect('login')
