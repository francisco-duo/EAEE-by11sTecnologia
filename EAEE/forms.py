from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import ComunicadoModel


class FormComunicadoModel(forms.ModelForm):

    class Meta:
        model = ComunicadoModel
        fildes = [
            'comunicado_usuario', 'comunicado_dt',
            'comunicado_mensagem',
        ]
