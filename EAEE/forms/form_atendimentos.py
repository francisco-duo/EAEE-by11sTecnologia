from django import forms
from EAEE.models import Agendamento


class AtendimentoForm(forms.ModelForm):
    
    class Meta:
        model = Agendamento
        fields = (
            'paciente',
            'especialidade',
            'dt_agendamento',
            'presente',
            'falta',
            'reposicao',
            'justificativa',
        )
