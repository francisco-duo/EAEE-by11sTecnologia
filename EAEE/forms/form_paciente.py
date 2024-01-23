from django import forms
from EAEE.models import PacienteModel


class PacienteForm(forms.ModelForm):

    class Meta:
        model = PacienteModel
        fields = (
            'paciente_nome',
            'paciente_foto',
            'paciente_dt_nascimento',
            'paciente_identidade',
            'paciente_medicacao',
            'paciente_exame',
            'paciente_exame_2',
            'paciente_exame_3',
        )
        exclude = ('paciente_dt_inscricao',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'
