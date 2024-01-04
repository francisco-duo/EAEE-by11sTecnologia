from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.models import User
from EAEE.models import PermissoesModel, ComunicadoModel


def inicio(request, usuario):
    if request.user.is_authenticated:
        return render(request, 'pages/sistema/inicio.html')
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