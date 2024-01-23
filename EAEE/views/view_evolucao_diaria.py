from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404

from EAEE.models import EvolucaoDiaria
from EAEE.forms import EvolucaoDiariaForm


def form_evolucao_diaria(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EvolucaoDiariaForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                return redirect('form_evolucao_diaria', request.user.username)
        return render(
            request,
            'pages/evolucao_diaria/form_evolucao_diaria.html',
            {'form': EvolucaoDiariaForm()}
        )
    else:
        return redirect('login')


def list_evolucao_diaria(request, usuario):
    if request.user.is_authenticated:
        evolucao_diaria = EvolucaoDiaria.objects.all().order_by('-id')
        paginator = Paginator(evolucao_diaria, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/evolucao_diaria/list_evolucao_diaria.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')


def edit_evolucao_diaria(request, usuario, pk):
    if request.user.is_authenticated:
        try:
            evolucao_diaria = EvolucaoDiaria.objects.get(id=pk)
            evolucao_diaria_form = EvolucaoDiariaForm(instance=evolucao_diaria)

        except EvolucaoDiaria.DoesNotExist:
            raise Http404('Devolutiva não encontrado')

        if request.method == 'POST':
            evolucao_diaria.save()

        return render(
            request,
            'pages/evolucao_diaria/edit_evolucao_diaria.html',
            {'evolucao_diaria_form': evolucao_diaria_form}
        )
    else:
        return redirect('login')


def search_evolucao_diaria(request, usuario):
    if request.user.is_authenticated:
        query = request.GET.get('q')
        evolucao_diaria = EvolucaoDiaria.objects.filter(
            paciente__paciente_nome__icontains=query
        )

        paginator = Paginator(evolucao_diaria, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/evolucao_diaria/search_evolucao_diaria.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')
