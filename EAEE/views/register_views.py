from django.shortcuts import render, redirect


def cadastrar_usuario(request, ):
    if request.user.is_authenticated:
        return render(request, 'pages/cadastrar_usuario.html')
    else:
        return redirect('login')
