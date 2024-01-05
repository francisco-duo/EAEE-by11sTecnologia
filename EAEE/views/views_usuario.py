from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.utils import timezone

from EAEE.models import PermissoesModel, ComunicadoModel, PacienteModel, RegistroFinanceiroModel, RegistroFinanceiroTipoModel


def inicio(request, usuario):
    if request.user.is_authenticated:
        comunicados = ComunicadoModel.objects.all().order_by('-id')
        paginator = Paginator(comunicados, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        mes_atual = timezone.now().month
        
        return render(request, 'pages/sistema/inicio.html', {'page_obj': page_obj, 'aniversariantes': PacienteModel.objects.filter(paciente_dt_nascimento__month=mes_atual)})
    else:
        return redirect('login')
    

def visualizar_comunicado(request, usuario, pk):
    if request.user.is_authenticated:
        return render(request, 'pages/comunicados.html', {'msg': ComunicadoModel.objects.get(id=pk)})
    else:
        return redirect('login')


def enviar_mensagem(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ComunicadoModel.objects.create(
                comunicado_usuario=request.user,
                comunicado_mensagem=request.POST.get('mensagem')
            )
            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/comunicados.html')
    else:
        return redirect('login')


def cadastrar_usuario(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('name')
            email = request.POST.get('email')

            senha = request.POST.get('password')
            confirma_senha = request.POST.get('confirm_password')

            if senha == confirma_senha:
                cadastro = User.objects.create_user(username, email, confirma_senha)
                cadastro.save()

            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/cadastrar_usuario.html')
    else:
        return redirect('login')


def cadastrar_usuario_permissoes(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            PermissoesModel.objects.create(
                usuario=User.objects.get(id=request.POST.get('usuario')),
                permissao=request.POST.get('permissao')
            )

            return redirect('inicio', usuario=request.user.username)
        return render(request, 'pages/cadastrar_usuario_permissao.html', {'usuarios': User.objects.all()})
    else:
        return redirect('login')
    

def pacientes(request, usuario):
    if request.user.is_authenticated:
        pacientes = PacienteModel.objects.all().order_by('-id')
        paginator = Paginator(pacientes, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'pages/patient_session_view.html', {'page_obj': page_obj})
    else:
        return redirect('login')
    
    
def pacientes_visualizar(request, usuario, pk):
    if request.user.is_authenticated:
        paciente = get_object_or_404(PacienteModel, id=pk)

        return render(request, 'pages/visualizar_paciente.html', {'paciente': paciente})
    else:
        return redirect('login')
    
    
def pacientes_busca(request, usuario):
    if request.user.is_authenticated:
        query = request.GET.get('q')
        pacientes = PacienteModel.objects.filter(
            paciente_nome__icontains=query
        )

        paginator = Paginator(pacientes, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'pages/patient_session_view.html', {'page_obj': page_obj})
    else:
        return redirect('login')
    

def financeiro(request, usuario):
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
                from datetime import datetime
                
                data = request.POST.get('data')
                valor = request.POST.get('valor')
                destino = request.POST.get('destino')
                tipo = request.POST.get('tipo')

                RegistroFinanceiroModel.objects.create(
                    registro_financeiro_funcionario=request.user,
                    registro_financeiro_valor=valor,
                    registro_financeiro_destino=destino,
                    registro_financeiro_tipo=RegistroFinanceiroTipoModel.objects.get(id=tipo),
                    registro_financeiro_dt=datetime.strptime(data, '%Y-%m-%d')
                )

                return redirect('financeiro', usuario=request.user.username)
            return render(request, 'pages/financeiro.html', {
                'tipo_financeiro': tipo_financeiro,
                'registros_financeiros': registros_financeiros,
                'valor_saida': valor_saida,
                'valor_entrada': valor_entrada
            })        
        return redirect('access')


def financeiro_search(request, usuario):
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
