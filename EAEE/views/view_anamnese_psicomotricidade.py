from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404

from EAEE.models import Psicomotricidade
from EAEE.forms import PsicomotricidadeForm


def form_anamnese_psicomotricidade(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PsicomotricidadeForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                return redirect('form_anamnese_psicomotricidade', request.user.username)
        return render(
            request,
            'pages/anamneses/psicomotricidade/form_anamnese_psicomotricidade.html',
            {'form': PsicomotricidadeForm()}
        )
    else:
        return redirect('login')


def list_anamnese_psicomotricidade(request, usuario):
    if request.user.is_authenticated:
        anamnese_psicomotricidade = Psicomotricidade.objects.all().order_by('-id')
        paginator = Paginator(anamnese_psicomotricidade, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/anamneses/psicomotricidade/list_anamnese_psicomotricidade.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')


def edit_anamnese_psicomotricidade(request, usuario, pk):
    if request.user.is_authenticated:
        try:
            anamnese_psicomotricidade = Psicomotricidade.objects.get(id=pk)
            anamnese_psicomotricidade_form = PsicomotricidadeForm(
                instance=anamnese_psicomotricidade)

        except Psicomotricidade.DoesNotExist:
            raise Http404('Anamnese não encontrado')

        if request.method == 'POST':
            anamnese_psicomotricidade_form.save()

        return render(
            request,
            'pages/anamneses/psicomotricidade/edit_anamnese_psicomotricidade.html',
            {'anamnese_psicomotricidade_form': anamnese_psicomotricidade_form}
        )
    else:
        return redirect('login')


def search_anamnese_psicomotricidade(request, usuario):
    if request.user.is_authenticated:
        query = request.GET.get('q')
        anamnese_psicomotricidade = Psicomotricidade.objects.filter(
            paciente__paciente_nome__icontains=query
        )

        paginator = Paginator(anamnese_psicomotricidade, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/anamneses/psicomotricidade/search_anamnese_psicomotricidade.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')
