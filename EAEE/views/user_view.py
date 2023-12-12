from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User

from ..models import ComunicadoModel, PacienteModel, PacienteRegistroModel, RegistroFinanceiroTipoModel, RegistroFinanceiroModel


def user_page(request, ):
    if request.user.is_authenticated:
        comunicados = ComunicadoModel.objects.all().order_by('-id')

        paginator = Paginator(comunicados, 4)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        if request.method == 'POST':
            obter_comunicado = request.POST.get('comunicado')
            print(obter_comunicado, type(obter_comunicado))

            comunicado_model = ComunicadoModel(
                comunicado_usuario=request.user, comunicado_mensagem=obter_comunicado
            )
            comunicado_model.save()

            return redirect('access')

        return render(request, 'pages/user.html', {
                'page_obj': page_obj
            })

    return redirect('login')


def patient_register(request, ):
    if request.user.is_authenticated:
        if request.method == 'POST':
            nome_paciente = request.POST.get('patient-name')
            nome_responsavel = request.POST.get('resp-patient-name')
            email = request.POST.get('patient-email')
            contato = request.POST.get('patient-contact')
            cpf = request.POST.get('patient-cpf')
            dt_nascimento = request.POST.get('patient-year')
            foto_paciente = request.FILES.get('patient-photo')
            exame_paciente = request.FILES.get('patient-file')
            exame_paciente_2 = request.FILES.get('patient-file2')
            exame_paciente_3 = request.FILES.get('patient-file3')

            contato_2 = request.POST.get('patient-contato_2')
            profissao = request.POST.get('patient-profissao')
            estado_civil = request.POST.get('patient-ec')
            nacionalidade = request.POST.get('patient-nacionalidade')
            endereco = request.POST.get('patient-endereco')
            cep = request.POST.get('patient-cep')
            estado = request.POST.get('patient-estado')
            cidade = request.POST.get('patient-cidade')
            
            paciente_model = PacienteModel(
                paciente_nome=nome_paciente,
                paciente_dt_nasc=dt_nascimento,
                paciente_responsavel_nome=nome_responsavel,
                paciente_responsavel_email=email,
                paciente_responsavel_contato=contato,
                paciente_responsavel_contato_2=contato_2,             
                paciente_responsavel_cpf=cpf,
                paciente_responsavel_nacionalidade=nacionalidade,
                paciente_responsavel_profissao=profissao,
                paciente_responsavel_estado_civil=estado_civil,
                paciente_responsavel_endereco=endereco,
                paciente_responsavel_cep=cep,
                paciente_responsavel_cidade=cidade,
                paciente_responsavel_estado=estado,
                paciente_exams=exame_paciente,
                paciente_exams_2=exame_paciente_2,
                paciente_exams_3=exame_paciente_3,
                paciente_foto=foto_paciente,
            )
            paciente_model.save()

            return redirect('access')

        return render(request, 'pages/patient_register.html', )

    return redirect('login')


def patient_view(request, ):
    if request.user.is_authenticated:
        pacientes = PacienteModel.objects.all()

        paginator = Paginator(pacientes, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'pages/patient_view.html', {'page_obj': page_obj})

    return redirect('/login/')


def patient_search_view(request, ):
    if request.user.is_authenticated:
        query = request.GET.get('q')
        pacientes = PacienteModel.objects.filter(
            paciente_nome__icontains=query
        )

        paginator = Paginator(pacientes, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'pages/patient_view_busca.html', {'page_obj': page_obj})

    return redirect('/login/')


def register_patients_sessions(request, ):
    if request.user.is_authenticated:
        paciente_list = PacienteModel.objects.all()

        if request.method == 'POST':
            PacienteRegistroModel.objects.create(
                paciente_registro_paciente=request.user,
                paciente_registro_queixa=request.POST.get('queixa'),
                paciente_registro_historico=PacienteModel.objects.get(id=request.POST.get('nome_paciente')),
                paciente_registro_procedimento_avaliativo=request.POST.get('procedimentos'),
                paciente_registro_observacao_clinica=request.POST.get('observacao'),
                paciente_registro_resultado=request.POST.get('resultado'),
                paciente_registro_conclusao=request.POST.get('conclusao'),
            )

            return redirect('access')
        return render(request, 'pages/register_patients_sessions.html', {
            'pacientes': paciente_list,
        })
    return redirect('/login/')


def patient_session_view(request, ):
    if request.user.is_authenticated:
        pacientes = PacienteRegistroModel.objects.all()

        paginator = Paginator(pacientes, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'pages/patient_session_view.html', {
            'page_obj': page_obj
        })
    return redirect('/login/')


def patient_session_search_view(request, ):
    if request.user.is_authenticated:
        query = request.GET.get('q')
        pacientes = PacienteRegistroModel.objects.filter(
            paciente_registro_historico__paciente_nome__icontains=query
        )

        paginator = Paginator(pacientes, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'pages/patient_session_view_busca.html', {'page_obj': page_obj})

    return redirect('/login/')


def financeiro(request, ):
    if request.user.is_authenticated:
        tipo_financeiro = RegistroFinanceiroTipoModel.objects.all()
        registros_financeiros = RegistroFinanceiroModel.objects.all().order_by('-id')

        valor_saida = 0
        valor_entrada = 0

        # Somando tipos de registro
        for registro in registros_financeiros:
            converte_tipo = float(registro.registro_financeiro_valor)
            
            if registro.registro_financeiro_tipo.id == 2:            
                valor_entrada += converte_tipo
            else:
                print('outro valor')
                valor_saida += converte_tipo

        if request.user.id == 1:
            if request.method == 'POST':
                data = request.POST.get('data')
                valor = request.POST.get('valor')
                destino = request.POST.get('destino')
                tipo = request.POST.get('tipo')

                RegistroFinanceiroModel.objects.create(
                    registro_financeiro_funcionario=request.user,
                    registro_financeiro_valor=valor,
                    registro_financeiro_destino=destino,
                    registro_financeiro_tipo=RegistroFinanceiroTipoModel.objects.get(id=tipo)
                )

                return redirect('financeiro')
            return render(request, 'pages/financeiro.html', {
                'tipo_financeiro': tipo_financeiro,
                'registros_financeiros': registros_financeiros,
                'valor_saida': valor_saida,
                'valor_entrada': valor_entrada
            })        
        return redirect('access')


def financeiro_search(request, ):
    if request.user.is_authenticated:
        
        tipo_financeiro = RegistroFinanceiroTipoModel.objects.all()
        mes = request.GET.get('mes')
        ano = request.GET.get('ano')
        registros = RegistroFinanceiroModel.objects.filter(
            data_filtro__year=ano, data_filtro__month=mes
        )
        
        # Soma total
        valor_saida = 0
        valor_entrada = 0

        # Somando tipos de registro
        for registro in registros:
            converte_tipo = float(registro.registro_financeiro_valor)
            
            if registro.registro_financeiro_tipo.id == 2:            
                valor_entrada += converte_tipo
            else:
                print('outro valor')
                valor_saida += converte_tipo

        paginator = Paginator(registros, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'pages/financeiro_search.html', {
            'page_obj': page_obj,
            'tipo_financeiro': tipo_financeiro,        
            'valor_saida': valor_saida,
            'valor_entrada': valor_entrada
            })

    return redirect('/login/')
