from django import forms
from EAEE.models import Devolutiva


class DevolutivaForm(forms.ModelForm):

    class Meta:
        model = Devolutiva
        fields = (
            'paciente',
            'anexo',
            'dt_devolutiva',
            'para',
            'sintese',
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'
