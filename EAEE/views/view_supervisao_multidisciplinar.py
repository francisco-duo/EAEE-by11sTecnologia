from datetime import datetime

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q

from EAEE.models import SupervisaoMultiprofissional
from EAEE.forms import SupervisaoMultiprofissionalForm


def form_supervisao_multidisciplinar(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SupervisaoMultiprofissionalForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                return redirect('form_supervisao_multidisciplinar', request.user.username)
        return render(
            request,
            'pages/supervisao_multidisciplinar/form_supervisao_multidisciplinar.html',
            {'form': SupervisaoMultiprofissionalForm()}
        )
    else:
        return redirect('login')


def list_supervisao_multidisciplinar(request, usuario):
    if request.user.is_authenticated:
        supervisao_multidisciplinar = SupervisaoMultiprofissional.objects.all().order_by('-id')
        paginator = Paginator(supervisao_multidisciplinar, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/supervisao_multidisciplinar/list_supervisao_multidisciplinar.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')


def edit_supervisao_multidisciplinar(request, usuario, pk):
    if request.user.is_authenticated:
        try:
            supervisao_multidisciplinar = SupervisaoMultiprofissional.objects.get(id=pk)
            supervisao_multidisciplinar_form = SupervisaoMultiprofissionalForm(instance=supervisao_multidisciplinar)

        except SupervisaoMultiprofissional.DoesNotExist:
            raise Http404('Supervisão não encontrado')

        if request.method == 'POST':
            if supervisao_multidisciplinar_form.is_valid():
                supervisao_multidisciplinar_form.save()

        return render(
            request,
            'pages/supervisao_multidisciplinar/edit_supervisao_multidisciplinar.html',
            {'supervisao_multidisciplinar_form': supervisao_multidisciplinar_form}
        )
    else:
        return redirect('login')


def search_supervisao_multidisciplinar(request, usuario):
    if request.user.is_authenticated:
        query = request.GET.get('q')

        supervisao_multidisciplinar = SupervisaoMultiprofissional.objects.filter(
            Q(paciente__paciente_nome__icontains=query)
            # Q(especialista__username__in=query)
        ).order_by('dt_registro')

        paginator = Paginator(supervisao_multidisciplinar, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/supervisao_multidisciplinar/search_supervisao_multidisciplinar.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')
