from django.shortcuts import render, redirect
from ..forms import FormComunicadoModel


def user_page(request, ):
    if request.user.is_authenticated:
        form = FormComunicadoModel(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return render(request, 'pages/user.html', )

    return redirect('/login/')


def patient_register(request, ):
    if request.user.is_authenticated:
        return render(request, 'pages/patient_register.html', )

    return redirect('/login/')


def patient_view(request, ):
    if request.user.is_authenticated:
        return render(request, 'pages/patient_view.html', )

    return redirect('/login/')


def register_patients_sessions(request, ):
    if request.user.is_authenticated:
        return render(request, 'pages/register_patients_sessions.html', )
    return redirect('/login/')
