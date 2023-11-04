from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


def app_login(request, ):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')

        user = authenticate(
            request, username=username, password=password
        )

        if user:
            login_django(request, user)
            return redirect('/app/')
        else:
            # Trocar esse return por uma message na interface
            return redirect('/login/')
    else:
        return render(request, 'pages/login.html')
