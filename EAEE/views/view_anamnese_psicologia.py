from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404

from EAEE.models import Psicologia
from EAEE.forms import PsicologiaForm


def form_anamnese_psicologia(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PsicologiaForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                return redirect('form_anamnese_psicologia', request.user.username)
        return render(
            request,
            'pages/anamneses/psicologia/form_psicologia.html',
            {'form': PsicologiaForm()}
        )
    else:
        return redirect('login')


def list_anamnese_psicologia(request, usuario):
    if request.user.is_authenticated:
        anamnese_psicologia = Psicologia.objects.all().order_by('-id')
        paginator = Paginator(anamnese_psicologia, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/anamneses/psicologia/list_psicologia.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')


def edit_anamnese_psicologia(request, usuario, pk):
    if request.user.is_authenticated:
        try:
            anamnese_psicologia = Psicologia.objects.get(id=pk)
            anamnese_psicologia_form = PsicologiaForm(
                instance=anamnese_psicologia)

        except Psicologia.DoesNotExist:
            raise Http404('Anamnese não encontrado')

        if request.method == 'POST':
            if anamnese_psicologia_form.is_valid():
                anamnese_psicologia_form.save()

        return render(
            request,
            'pages/anamneses/psicologia/edit_psicologia.html',
            {'anamnese_psicologia_form': anamnese_psicologia_form}
        )
    else:
        return redirect('login')


def search_anamnese_psicologia(request, usuario):
    if request.user.is_authenticated:
        query = request.GET.get('q')
        anamnese_psicologia = Psicologia.objects.filter(
            paciente__paciente_nome__icontains=query
        )

        paginator = Paginator(anamnese_psicologia, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/anamneses/psicologia/search_psicologia.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')
