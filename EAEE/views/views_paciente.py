from django.shortcuts import HttpResponse, render, redirect
from EAEE.models import PacienteModel, TipoDeVinculoComPacienteModels, Psicopedagogia


def teste(request, ):
    return redirect('site')


def cadastrar_novo_paciente(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            PacienteModel.objects.create(
                paciente_nome=request.POST.get('nome'),
                paciente_foto=request.POST.get('foto'),
                paciente_dt_nascimento=request.POST.get('idade'),
                paciente_identidade=request.POST.get('identidade'),
                paciente_exame=request.POST.get('exame'),
                paciente_exame_2=request.POST.get('exame2'),
                paciente_exame_3=request.POST.get('exame3'),
                escola=request.POST.get('escola'),
                serie=request.POST.get('serie'),
                turno=request.POST.get('turno'),
                gravidez=request.POST.get('gravidez'),
                fatos_marcantes=request.POST.get('fatos_marcantes'),
                condicoes_emocionais=request.POST.get('condicoes_emocionais'),
                pos_parto=request.POST.get('pos_parto'),
                parto=request.POST.get('parto'),
                semanas=request.POST.get('semanas'),
                peso=request.POST.get('peso'),
                altura=request.POST.get('altura'),
                cuidados_parto=request.POST.get('cuidados_parto'),
                apgar1=request.POST.get('apgar1'),
                apgar5=request.POST.get('apgar5'),
                succao=request.POST.get('amamentacao'),
                leite_marterno=request.POST.get('leite_materno'),
                usou_mamadeira=request.POST.get('mamadeira'),
                alimento_atual=request.POST.get('alimentacao_atual'),
                recebe_ajuda=request.POST.get('recebe_ajuda'),
                sono=request.POST.get('sono'),
                baba=request.POST.get('baba'),
                acorda=request.POST.get('acorda'),
                fala_dormindo=request.POST.get('fala_dormindo'),
                dorme_sozinho=request.POST.get('dorme_sozinho'),
                horario_de_dormir=request.POST.get('horario_de_dormir'),
                esfincteres=request.POST.get('esfincteres'),
                fobias=request.POST.get('fobias'),
                mora=request.POST.get('mora'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/pacientes/cadastro_paciente.html')
    else:
        return redirect('login')


def cadastrar_responsavel(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            TipoDeVinculoComPacienteModels.objects.create(
                paciente=PacienteModel.objects.get(id=request.POST.get('paciente')),
                paciente_filiacao_nome=request.POST.get('patient-name'),
                paciente_filiacao_tipo_vinculo=request.POST.get('vinculo'),
                paciente_filiacao_email=request.POST.get('patient-email'),
                paciente_filiacao_dt_nascimento=request.POST.get('patient-year'),
                paciente_filiacao_contato_telefone_pessoal=request.POST.get('contato'),
                paciente_filiacao_contato_telefone_empresa=request.POST.get('contato2'),
                paciente_filiacao_cpf=request.POST.get('patient-cpf'),
                paciente_filiacao_nacionalidade=request.POST.get('patient-nacionalidade'),
                paciente_filiacao_profissao=request.POST.get('patient-profissao'),
                paciente_filiacao_estado_civil=request.POST.get('patient-ec'),
                paceinte_filiacao_endereco=request.POST.get('patient-endereco'),
                paceinte_filiacao_cep=request.POST.get('patient-cep'),
                paceinte_filiacao_comprovante_residencia=request.POST.get('patient-file'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/pacientes/cadastro_responsavel.html', {'pacientes': PacienteModel.objects.all().order_by('-id')})
    else:
        return redirect('login')


def anamnese_psicopedagogia(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            TipoDeVinculoComPacienteModels.objects.create(
                paciente=PacienteModel.objects.get(id=request.POST.get('paciente')),
                idade_que_comecou_a_frequentar_escola=request.POST.get('idade_que_frequentou_a_escola'),
                como_foi_adaptacao=request.POST.get('patient-name'),
                reprovou=request.POST.get('vinculo'),
                ralacao_professores_colegas=request.POST.get('patient-email'),
                motivado_escola=request.POST.get('patient-year'),
                falta_assiduo=request.POST.get('contato'),
                realiza_atividades_com_satisfacao=request.POST.get('contato2'),
                precisa_ajuda=request.POST.get('patient-cpf'),
                predilecao_matematica_portugues=request.POST.get('patient-nacionalidade'),
                dificuldades_aprendizagem=request.POST.get('patient-profissao'),
                antecedentes_com_dificuldade=request.POST.get('patient-ec'),
                queixas_comuns_escola=request.POST.get('patient-endereco'),
                fala_compreensivel=request.POST.get('patient-cep'),
                troca_ou_omissao_fonemas=request.POST.get('patient-file'),
                conta_historia=request.POST.get('patient-file'),
                corporalmente_desenvolto=request.POST.get('patient-file'),
                anda_bicicleta=request.POST.get('patient-file'),
                organizado=request.POST.get('patient-file'),
                ajuda_em_casa=request.POST.get('patient-file'),
                censurado=request.POST.get('patient-file'),
                brinquedos_favorito=request.POST.get('patient-file'),
                gosta_desenhar=request.POST.get('patient-file'),
                uso_de_eletronicos=request.POST.get('patient-file'),
                horas_livres=request.POST.get('patient-file'),
                potencialidades_marcantes=request.POST.get('patient-file'),
                fragilidades_evidentes=request.POST.get('patient-file'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/anamnese_psicopedagogia.html')
    else:
        return redirect('login')


def anamnese_psicologia(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            TipoDeVinculoComPacienteModels.objects.create(
                paciente=PacienteModel.objects.get(id=request.POST.get('paciente')),
                numero_irmaos=request.POST.get('qnt_irmaos'),
                reacao_nascimento_irmao=request.POST.get('reacao_nascimento'),
                relacionamento_irmaos=request.POST.get('relacionamento_irmaos'),
                relacionamento_pais=request.POST.get('relacionamento_pais'),
                relacionamento_familia=request.POST.get('relacionamento_familia'),
                personalidade=request.POST.get('personalidade'),
                comportamento_roer_unhas=request.POST.get('comportamento'),
                humor_habitual=request.POST.get('humor'),
                brinca_sozinho_ou_grupo=request.POST.get('brincar_sozinho'),
                estranha_mudancas_ambiente=request.POST.get('mudanca_humor'),
                aceita_seguir_comandos=request.POST.get('seguir_comandos'),
                brincadeiras_brinquedo_favorito=request.POST.get('brincadeiras'),
                gosta_de_musicas=request.POST.get('gosta_musica'),
                baste_cabeca_na_parede=request.POST.get('bate_parede'),
                atitudes_desse_habito=request.POST.get('habito'),
                reprovou_na_escola=request.POST.get('reprovou'),
                relacionamento_colegas=request.POST.get('relacionamento_escola'),
                relacionamento_professores=request.POST.get('relacionamento_professores'),
                idade_desfralde=request.POST.get('idade_desfraude'),
                dificuldades_desfraude=request.POST.get('desfraude_dificuldades'),
                higiene_sozinho=request.POST.get('higiene'),
                idade_higiene_sozinho=request.POST.get('banho'),
                problema_na_fala=request.POST.get('problema_fala'),
                troca_letras=request.POST.get('troca_letras'),
                acorda_vai_para_cama_dos_pais=request.POST.get('cama_dos_pais'),
                dorme_sozinho=request.POST.get('medo_dormir_sozinho'),
                objeto_para_dormir=request.POST.get('objeto_para_dormir'),
                urina_na_cama=request.POST.get('urina_na_cama'),
                horario_para_refeicoes=request.POST.get('horario_refeicoes'),
                refeicoes_em_familia=request.POST.get('refeicoes_familia'),
                local=request.POST.get('local'),
                assiste_enquanto_come=request.POST.get('assite_enquanto_come'),
                como_se_alimenta=request.POST.get('como_se_alimenta'),
                seletividade_alimentar=request.POST.get('seletividade_alimentar'),
                curiosidade_sexual=request.POST.get('curiosidade_sexual'),
                atitude_dos_pais=request.POST.get('atitude_dos_pais'),
                # informacoes_sexuais=request.POST.get('tratamento_medico'),
                tratamento_medico=request.POST.get('tratamento_medico'),
                internado=request.POST.get('esteve_internado'),
                motivo_internação=request.POST.get('motivo_internacao'),
                operado=request.POST.get('foi_operado'),
                idade_operado=request.POST.get('idade_operado'),
                adoece_facilmente=request.POST.get('adoece'),
                acompanhamento_psicologico=request.POST.get('faz_acompanhamento'),
                encaminhamento=request.POST.get('encaminhamento'),
                algum_membro_ja_fez_acompanhamento_psicologico=request.POST.get('membro_acompanhamento'),
                queixa_psicologica_principal=request.POST.get('queixa'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/anamnese_psicologia.html')
    else:
        return redirect('login')


def anamnese_fonoaudiologia(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            TipoDeVinculoComPacienteModels.objects.create(
                paciente=PacienteModel.objects.get(id=request.POST.get('paciente')),
                encaminhado=request.POST.get('Encaminhado por'),
                queixa=request.POST.get('Queixa'),
                tratamento_anterior=request.POST.get('Tratamentos anteriores'),
                quando_comecou_sentar=request.POST.get('Quando começou a sentar'),
                quando_engatinhou=request.POST.get('Quando começou a engatinhar'),
                quando_andou=request.POST.get('Quando começou a andar'),
                quando_comeu=request.POST.get('Quando começou a comer'),
                quando_balburciou=request.POST.get('Quando começou a balbuciar?'),
                primeiras_palavras=request.POST.get('Primeiras palavras'),
                articulacao_palavras=request.POST.get('Articula bem'),
                regressao_linguistica=request.POST.get('Houve alguma regressão da linguagem em algum momento'),
                comunicacao_atual=request.POST.get('Como é a comunicação atualmente'),
                mamadeira_chupeta=request.POST.get('Como é a comunicação atualmente'),
                horas_de_sono=request.POST.get('Dorme por quantas horas?'),
                autonomia_dormir=request.POST.get('Tem autonomia para dormir?'),
                doencas_alergias=request.POST.get('Doenças / alergias?'),
                acompanhamento_medico=request.POST.get('Faz algum acompanhamento médico atualmente?'),
                acompanhamento_fonoaudiologico=request.POST.get('Já fez acompanhamento fonoaudiológico? Quando?'),
                exames_fonoaudiologicos=request.POST.get('Já fez exames audiológicos?'),
                teste_orelinha=request.POST.get('Já fez teste da orelhinha?'),
                idade_comecou_escola=request.POST.get('Iniciou com que idade?'),
                alfabetizado=request.POST.get('Alfabetizado?'),
                materia_mais_gosta=request.POST.get('Matéria que mais gosta?'),
                relacionamento_pais=request.POST.get('Como é o relacionamento com os pais?'),
                relacionamento_criancas=request.POST.get('Como se relaciona com outras crianças?'),
                hobby=request.POST.get('O que gosta de fazer (hobby)?'),
                familiar_dificuldades_na_fala=request.POST.get('Alguém na família apresenta/ apresentou dificuldade na fala?'),
                prende_atencao=request.POST.get('O que prende a atenção?'),
                gosta_de_brincar=request.POST.get('Com o que gosta de brincar?'),
                compreende_comandos=request.POST.get('Atende e compreende comandos?'),
                contato_visual=request.POST.get('Faz contato visual?'),
                interage=request.POST.get('Interage?'),
                atencao_por_tempo_significativo=request.POST.get('Mantém a atenção em uma atividade por um tempo significativo?'),
                expectativa_do_acompanhamento_fonoaudiologico=request.POST.get('Qual a expectativa com o acompanhamento fonoaudiológico?'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/anamnese_fonoaudiologia.html')
    else:
        return redirect('login')


def anamnese_psicomotricidade(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            TipoDeVinculoComPacienteModels.objects.create(
                paciente=PacienteModel.objects.get(id=request.POST.get('paciente')),
                paciente_filiacao_nome=request.POST.get('patient-name'),
                paciente_filiacao_tipo_vinculo=request.POST.get('vinculo'),
                paciente_filiacao_email=request.POST.get('patient-email'),
                paciente_filiacao_dt_nascimento=request.POST.get('patient-year'),
                paciente_filiacao_contato_telefone_pessoal=request.POST.get('contato'),
                paciente_filiacao_contato_telefone_empresa=request.POST.get('contato2'),
                paciente_filiacao_cpf=request.POST.get('patient-cpf'),
                paciente_filiacao_nacionalidade=request.POST.get('patient-nacionalidade'),
                paciente_filiacao_profissao=request.POST.get('patient-profissao'),
                paciente_filiacao_estado_civil=request.POST.get('patient-ec'),
                paceinte_filiacao_endereco=request.POST.get('patient-endereco'),
                paceinte_filiacao_cep=request.POST.get('patient-cep'),
                paceinte_filiacao_comprovante_residencia=request.POST.get('patient-file'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/anamnese_psicomotricidade.html')
    else:
        return redirect('login')
    

def devolutiva(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            TipoDeVinculoComPacienteModels.objects.create(
                paciente=PacienteModel.objects.get(id=request.POST.get('paciente')),
                paciente_filiacao_nome=request.POST.get('patient-name'),
                paciente_filiacao_tipo_vinculo=request.POST.get('vinculo'),
                paciente_filiacao_email=request.POST.get('patient-email'),
                paciente_filiacao_dt_nascimento=request.POST.get('patient-year'),
                paciente_filiacao_contato_telefone_pessoal=request.POST.get('contato'),
                paciente_filiacao_contato_telefone_empresa=request.POST.get('contato2'),
                paciente_filiacao_cpf=request.POST.get('patient-cpf'),
                paciente_filiacao_nacionalidade=request.POST.get('patient-nacionalidade'),
                paciente_filiacao_profissao=request.POST.get('patient-profissao'),
                paciente_filiacao_estado_civil=request.POST.get('patient-ec'),
                paceinte_filiacao_endereco=request.POST.get('patient-endereco'),
                paceinte_filiacao_cep=request.POST.get('patient-cep'),
                paceinte_filiacao_comprovante_residencia=request.POST.get('patient-file'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/devolutiva.html')
    else:
        return redirect('login')


def reunioes_externas(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            TipoDeVinculoComPacienteModels.objects.create(
                paciente=PacienteModel.objects.get(id=request.POST.get('paciente')),
                paciente_filiacao_nome=request.POST.get('patient-name'),
                paciente_filiacao_tipo_vinculo=request.POST.get('vinculo'),
                paciente_filiacao_email=request.POST.get('patient-email'),
                paciente_filiacao_dt_nascimento=request.POST.get('patient-year'),
                paciente_filiacao_contato_telefone_pessoal=request.POST.get('contato'),
                paciente_filiacao_contato_telefone_empresa=request.POST.get('contato2'),
                paciente_filiacao_cpf=request.POST.get('patient-cpf'),
                paciente_filiacao_nacionalidade=request.POST.get('patient-nacionalidade'),
                paciente_filiacao_profissao=request.POST.get('patient-profissao'),
                paciente_filiacao_estado_civil=request.POST.get('patient-ec'),
                paceinte_filiacao_endereco=request.POST.get('patient-endereco'),
                paceinte_filiacao_cep=request.POST.get('patient-cep'),
                paceinte_filiacao_comprovante_residencia=request.POST.get('patient-file'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/reunioes_externas.html')
    else:
        return redirect('login')


def encaminhamento(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            TipoDeVinculoComPacienteModels.objects.create(
                paciente=PacienteModel.objects.get(id=request.POST.get('paciente')),
                paciente_filiacao_nome=request.POST.get('patient-name'),
                paciente_filiacao_tipo_vinculo=request.POST.get('vinculo'),
                paciente_filiacao_email=request.POST.get('patient-email'),
                paciente_filiacao_dt_nascimento=request.POST.get('patient-year'),
                paciente_filiacao_contato_telefone_pessoal=request.POST.get('contato'),
                paciente_filiacao_contato_telefone_empresa=request.POST.get('contato2'),
                paciente_filiacao_cpf=request.POST.get('patient-cpf'),
                paciente_filiacao_nacionalidade=request.POST.get('patient-nacionalidade'),
                paciente_filiacao_profissao=request.POST.get('patient-profissao'),
                paciente_filiacao_estado_civil=request.POST.get('patient-ec'),
                paceinte_filiacao_endereco=request.POST.get('patient-endereco'),
                paceinte_filiacao_cep=request.POST.get('patient-cep'),
                paceinte_filiacao_comprovante_residencia=request.POST.get('patient-file'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/encaminhamento.html')
    else:
        return redirect('login')


def evolucao_diaria(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            TipoDeVinculoComPacienteModels.objects.create(
                paciente=PacienteModel.objects.get(id=request.POST.get('paciente')),
                paciente_filiacao_nome=request.POST.get('patient-name'),
                paciente_filiacao_tipo_vinculo=request.POST.get('vinculo'),
                paciente_filiacao_email=request.POST.get('patient-email'),
                paciente_filiacao_dt_nascimento=request.POST.get('patient-year'),
                paciente_filiacao_contato_telefone_pessoal=request.POST.get('contato'),
                paciente_filiacao_contato_telefone_empresa=request.POST.get('contato2'),
                paciente_filiacao_cpf=request.POST.get('patient-cpf'),
                paciente_filiacao_nacionalidade=request.POST.get('patient-nacionalidade'),
                paciente_filiacao_profissao=request.POST.get('patient-profissao'),
                paciente_filiacao_estado_civil=request.POST.get('patient-ec'),
                paceinte_filiacao_endereco=request.POST.get('patient-endereco'),
                paceinte_filiacao_cep=request.POST.get('patient-cep'),
                paceinte_filiacao_comprovante_residencia=request.POST.get('patient-file'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/evolucao_diaria.html')
    else:
        return redirect('login')


def supervisao_multiprofissional(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            TipoDeVinculoComPacienteModels.objects.create(
                paciente=PacienteModel.objects.get(id=request.POST.get('paciente')),
                paciente_filiacao_nome=request.POST.get('patient-name'),
                paciente_filiacao_tipo_vinculo=request.POST.get('vinculo'),
                paciente_filiacao_email=request.POST.get('patient-email'),
                paciente_filiacao_dt_nascimento=request.POST.get('patient-year'),
                paciente_filiacao_contato_telefone_pessoal=request.POST.get('contato'),
                paciente_filiacao_contato_telefone_empresa=request.POST.get('contato2'),
                paciente_filiacao_cpf=request.POST.get('patient-cpf'),
                paciente_filiacao_nacionalidade=request.POST.get('patient-nacionalidade'),
                paciente_filiacao_profissao=request.POST.get('patient-profissao'),
                paciente_filiacao_estado_civil=request.POST.get('patient-ec'),
                paceinte_filiacao_endereco=request.POST.get('patient-endereco'),
                paceinte_filiacao_cep=request.POST.get('patient-cep'),
                paceinte_filiacao_comprovante_residencia=request.POST.get('patient-file'),
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/supervisao_multiprofissional.html')
    else:
        return redirect('login')