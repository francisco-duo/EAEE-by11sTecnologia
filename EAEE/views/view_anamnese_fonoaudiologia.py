from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404

from EAEE.models import Fonoaudiologia
from EAEE.forms import FonoaudiologiaForm


def form_anamnese_fonoaudiologia(request, usuario):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FonoaudiologiaForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                return redirect('form_anamnese_fonoaudiologia', request.user.username)
        return render(
            request,
            'pages/anamneses/fonoaudiologia/form_fonoaudiologia.html',
            {'form': FonoaudiologiaForm()}
        )
    else:
        return redirect('login')


def list_anamnese_fonoaudiologia(request, usuario):
    if request.user.is_authenticated:
        anamnese_fonoaudiologia = Fonoaudiologia.objects.all().order_by('-id')
        paginator = Paginator(anamnese_fonoaudiologia, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/anamneses/fonoaudiologia/list_fonoaudiologia.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')


def edit_anamnese_fonoaudiologia(request, usuario, pk):
    if request.user.is_authenticated:
        try:
            anamnese_fonoaudiologia = Fonoaudiologia.objects.get(id=pk)
            anamnese_fonoaudiologia_form = FonoaudiologiaForm(
                instance=anamnese_fonoaudiologia)
            
            if request.method == 'POST':
                if anamnese_fonoaudiologia_form.is_valid():
                    anamnese_fonoaudiologia_form.save()

        except Fonoaudiologia.DoesNotExist:
            raise Http404('Devolutiva não encontrado')

        return render(
            request,
            'pages/anamneses/fonoaudiologia/edit_fonoaudiologia.html',
            {'anamnese_fonoaudiologia_form': anamnese_fonoaudiologia_form}
        )
    else:
        return redirect('login')


def search_anamnese_fonoaudiologia(request, usuario):
    if request.user.is_authenticated:
        query = request.GET.get('q')
        anamnese_fonoaudiologia = Fonoaudiologia.objects.filter(
            paciente__paciente_nome__icontains=query
        )

        paginator = Paginator(anamnese_fonoaudiologia, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'pages/anamneses/fonoaudiologia/search_fonoaudiologia.html',
            {'page_obj': page_obj}
        )
    else:
        return redirect('login')
