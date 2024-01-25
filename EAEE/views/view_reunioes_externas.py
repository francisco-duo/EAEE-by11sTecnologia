from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404

from EAEE.models import ReunioesExternas
from EAEE.forms import ReunioesExternasForms


def form_reunioes_externas(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReunioesExternasForms(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                return redirect('form_reunioes_externas', request.user.username)
        return render(
            request,
            'pages/reunioes_externas/form_reunioes_externas.html',
            {'form': ReunioesExternasForms()}
        )
    else:
        return redirect('login')


def list_reunioes_externas(request, usuario):
    if request.user.is_authenticated:
        reunioes_externas = ReunioesExternas.objects.all().order_by('-id')
        paginator = Paginator(reunioes_externas, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/reunioes_externas/list_reunioes_externas.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')


def edit_reunioes_externas(request, usuario, pk):
    if request.user.is_authenticated:
        try:
            reunioes_externas = ReunioesExternas.objects.get(id=pk)
            reunioes_externas_form = ReunioesExternasForms(instance=reunioes_externas)

        except ReunioesExternas.DoesNotExist:
            raise Http404('Devolutiva não encontrado')

        if request.method == 'POST':
            if reunioes_externas_form.is_valid():
                reunioes_externas_form.save()

        return render(
            request,
            'pages/reunioes_externas/edit_reunioes_externas.html',
            {'reunioes_externas_form': reunioes_externas_form}
        )
    else:
        return redirect('login')


def search_reunioes_externas(request, usuario):
    if request.user.is_authenticated:
        query = request.GET.get('q')
        reunioes_externas = ReunioesExternas.objects.filter(
            paciente__paciente_nome__icontains=query
        )

        paginator = Paginator(reunioes_externas, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/reunioes_externas/search_reunioes_externas.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')
