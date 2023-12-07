from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User

from ..models import ComunicadoModel, PacienteModel, PacienteRegistroModel


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

            paciente_model = PacienteModel(
                paciente_nome=nome_paciente,
                paciente_dt_nasc=dt_nascimento,
                paciente_responsavel_nome=nome_responsavel,
                paciente_responsavel_email=email,
                paciente_responsavel_contato=contato,
                paciente_responsavel_cpf=cpf,
                paciente_exams=exame_paciente,
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
                paciente_registro_paciente = request.user,
                paciente_registro_queixa = request.POST.get('queixa'),
                paciente_registro_historico = PacienteModel.objects.get(id=request.POST.get('nome_paciente')),
                paciente_registro_procedimento_avaliativo = request.POST.get('procedimentos'),
                paciente_registro_observacao_clinica = request.POST.get('observacao'),
                paciente_registro_resultado = request.POST.get('resultado'),
                paciente_registro_conclusao = request.POST.get('conclusao'),
            )

            return redirect('access')
        return render(request, 'pages/register_patients_sessions.html', {
            'pacientes': paciente_list,
        })
    return redirect('/login/')
