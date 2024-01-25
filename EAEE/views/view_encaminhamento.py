from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404

from EAEE.models import Encaminhamento
from EAEE.forms import EncaminhamentoForms


def form_encaminhamento(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EncaminhamentoForms(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                return redirect('view_encaminhamento', request.user.username)
        return render(
            request,
            'pages/encaminhamento/form_encaminhamento.html',
            {'form': EncaminhamentoForms()}
        )
    else:
        return redirect('login')


def list_encaminhamento(request, usuario):
    if request.user.is_authenticated:
        pacientes = Encaminhamento.objects.all().order_by('-id')
        paginator = Paginator(pacientes, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/encaminhamento/list_encaminhamento.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')


def edit_encaminhamento(request, usuario, pk):
    if request.user.is_authenticated:
        try:
            encaminhamento = Encaminhamento.objects.get(id=pk)
            encaminhamento_form = EncaminhamentoForms(instance=encaminhamento)

        except Encaminhamento.DoesNotExist:
            raise Http404('Devolutiva não encontrado')

        if request.method == 'POST':
            if encaminhamento_form.is_valid():
                encaminhamento_form.save()

        return render(
            request,
            'pages/encaminhamento/edit_encaminhamento.html',
            {'encaminhamento_form': encaminhamento_form}
        )
    else:
        return redirect('login')


def search_encaminhamento(request, usuario):
    if request.user.is_authenticated:
        query = request.GET.get('q')
        encaminhamento = Encaminhamento.objects.filter(
            paciente__paciente_nome__icontains=query
        )

        paginator = Paginator(encaminhamento, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/encaminhamento/search_encaminhamento.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')
