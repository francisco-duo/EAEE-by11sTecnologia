from django import forms
from EAEE.models import EvolucaoDiaria


class EvolucaoDiariaForm(forms.ModelForm):

    class Meta:
        model = EvolucaoDiaria
        fields = (
            'paciente',
            'anexo',
            'dt_devolutiva',
            'sintese',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'