from django.shortcuts import render, redirect


def user_page(request, user_name: str, ):
    if request.user.is_authenticated:
        context_user = {
            "username": request.user.username
        }

        return render(request, 'pages/user.html', {"context_user": context_user})

    return redirect('/login/')
