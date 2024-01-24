from django import forms
from EAEE.models import Fonoaudiologia


class FonoaudiologiaForm(forms.ModelForm):

    class Meta:
        model = Fonoaudiologia
        fields = '__all__'
        exclude = ('dt_registro', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'
