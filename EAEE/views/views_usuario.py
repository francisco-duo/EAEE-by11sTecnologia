from django.shortcuts import HttpResponse, render, redirect


def inicio(request, usuario):
    if request.user.is_authenticated:
        return render(request, 'pages/sistema/inicio.html')
    else:
        return redirect('login')
