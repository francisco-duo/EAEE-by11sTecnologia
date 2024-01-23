from django import forms
from EAEE.models import SupervisaoMultiprofissional


class SupervisaoMultiprofissionalForm(forms.ModelForm):

    class Meta:
        model = SupervisaoMultiprofissional
        fields = (
            'paciente',
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'