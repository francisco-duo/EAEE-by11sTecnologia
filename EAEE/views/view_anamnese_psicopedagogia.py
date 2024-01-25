from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404

from EAEE.models import Psicopedagogia
from EAEE.forms import PsicopedagogiaForm


def form_anamnese_psicopedagogia(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PsicopedagogiaForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                return redirect('form_anamnese_psicopedagogia', request.user.username)
        return render(
            request,
            'pages/anamneses/psicopedagogia/form_psicopedagogia.html',
            {'form': PsicopedagogiaForm()}
        )
    else:
        return redirect('login')


def list_anamnese_psicopedagogia(request, usuario):
    if request.user.is_authenticated:
        anamnese_psicopedagogia = Psicopedagogia.objects.all().order_by('-id')
        paginator = Paginator(anamnese_psicopedagogia, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/anamneses/psicopedagogia/list_psicopedagogia.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')


def edit_anamnese_psicopedagogia(request, usuario, pk):
    if request.user.is_authenticated:
        try:
            anamnese_psicopedagogia = Psicopedagogia.objects.get(id=pk)
            anamnese_psicopedagogia_form = PsicopedagogiaForm(instance=anamnese_psicopedagogia)

        except Psicopedagogia.DoesNotExist:
            raise Http404('Anamnese não encontrado')

        if request.method == 'POST':
            if anamnese_psicopedagogia_form.is_valid():
                anamnese_psicopedagogia_form.save()

        return render(
            request,
            'pages/anamneses/psicopedagogia/edit_psicopedagogia.html',
            {'anamnese_psicopedagogia_form': anamnese_psicopedagogia_form}
        )
    else:
        return redirect('login')


def search_anamnese_psicopedagogia(request, usuario):
    if request.user.is_authenticated:
        query = request.GET.get('q')
        anamnese_psicopedagogia = Psicopedagogia.objects.filter(
            paciente__paciente_nome__icontains=query
        )

        paginator = Paginator(anamnese_psicopedagogia, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/anamneses/psicopedagogia/search_psicopedagogia.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')
