from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404

from EAEE.models import TerapiaOcupacional
from EAEE.forms import TerapiaOcupacionalForm


def form_anamnese_terapia_ocupacional(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TerapiaOcupacionalForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                return redirect('form_anamnese_terapia_ocupacional', request.user.username)
        return render(
            request,
            'pages/anamneses/terapia_ocupacional/form_terapia_ocupacional.html',
            {'form': TerapiaOcupacionalForm()}
        )
    else:
        return redirect('login')


def list_anamnese_terapia_ocupacional(request, usuario):
    if request.user.is_authenticated:
        anamnese_terapia_ocupacional = TerapiaOcupacional.objects.all().order_by('-id')
        paginator = Paginator(anamnese_terapia_ocupacional, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/anamneses/terapia_ocupacional/list_terapia_ocupacional.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')


def edit_anamnese_terapia_ocupacional(request, usuario, pk):
    if request.user.is_authenticated:
        try:
            anamnese_terapia_ocupacional = TerapiaOcupacional.objects.get(id=pk)
            anamnese_terapia_ocupacional_form = TerapiaOcupacionalForm(instance=anamnese_terapia_ocupacional)

        except TerapiaOcupacional.DoesNotExist:
            raise Http404('Anamnese não encontrado')

        if request.method == 'POST':
            if anamnese_terapia_ocupacional_form.is_valid():
                anamnese_terapia_ocupacional_form.save()

        return render(
            request,
            'pages/anamneses/terapia_ocupacional/edit_terapia_ocupacional.html',
            {'anamnese_terapia_ocupacional_form': anamnese_terapia_ocupacional_form}
        )
    else:
        return redirect('login')


def search_anamnese_terapia_ocupacional(request, usuario):
    if request.user.is_authenticated:
        query = request.GET.get('q')
        anamnese_terapia_ocupacional = TerapiaOcupacional.objects.filter(
            paciente__paciente_nome__icontains=query
        )

        paginator = Paginator(anamnese_terapia_ocupacional, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/anamneses/terapia_ocupacional/search_terapia_ocupacional.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')
