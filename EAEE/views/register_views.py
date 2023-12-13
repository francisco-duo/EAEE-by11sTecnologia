from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def cadastrar_usuario(request, ):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('name')
            email = request.POST.get('email')

            senha = request.POST.get('password')
            confirma_senha = request.POST.get('confirm_password')

            if senha == confirma_senha:
                cadastro = User.objects.create_user(username, email, confirma_senha)
                cadastro.save()

            return redirect('access')

        return render(request, 'pages/cadastrar_usuario.html')
    else:
        return redirect('login')
