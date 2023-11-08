from django.shortcuts import render, redirect


def user_page(request, ):
    if request.user.is_authenticated:
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
