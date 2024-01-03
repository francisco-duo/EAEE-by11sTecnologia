from django.shortcuts import HttpResponse, render, redirect
from EAEE.models import PacienteModel, TipoDeVinculoComPacienteModels


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
                paciente_exame_3=request.POST.get('exame3')
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/pacientes/cadastro_paciente.html')
    else:
        return redirect('login')


def cadastrar_responsavel(request, usuario):
    if request.user.is_authenticated:
        return render(request, 'pages/pacientes/cadastro_responsavel.html')
    else:
        return redirect('login')


def anamnese_psicopedagogia(request, usuario):
    if request.user.is_authenticated:
        return render(request, 'pages/anamnese_psicopedagogia.html')
    else:
        return redirect('login')


def anamnese_psicologia(request, usuario):
    if request.user.is_authenticated:
        return render(request, 'pages/anamnese_psicologia.html')
    else:
        return redirect('login')


def anamnese_fonoaudiologia(request, usuario):
    if request.user.is_authenticated:
        return render(request, 'pages/anamnese_fonoaudiologia.html')
    else:
        return redirect('login')


def anamnese_psicomotricidade(request, usuario):
    if request.user.is_authenticated:
        return render(request, 'pages/anamnese_psicomotricidade.html')
    else:
        return redirect('login')
    

def devolutiva(request, usuario):
    if request.user.is_authenticated:
        return render(request, 'pages/devolutiva.html')
    else:
        return redirect('login')


def reunioes_externas(request, usuario):
    if request.user.is_authenticated:
        return render(request, 'pages/reunioes_externas.html')
    else:
        return redirect('login')


def encaminhamento(request, usuario):
    if request.user.is_authenticated:
        return render(request, 'pages/encaminhamento.html')
    else:
        return redirect('login')


def evolucao_diaria(request, usuario):
    if request.user.is_authenticated:
        return render(request, 'pages/evolucao_diaria.html')
    else:
        return redirect('login')


def supervisao_multiprofissional(request, usuario):
    if request.user.is_authenticated:
        return render(request, 'pages/supervisao_multiprofissional.html')
    else:
        return redirect('login')