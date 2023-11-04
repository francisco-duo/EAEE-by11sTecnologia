from django.shortcuts import HttpResponse, redirect


def user_page(request, user_name: str, ):
    if request.user.is_authenticated:
        return HttpResponse(f'Bem vindo - {user_name}')

    return redirect('/login/')
