from django import forms
from EAEE.models import InformacoesComplementares


class InformacoesComplementaresForm(forms.ModelForm):

    class Meta:
        model = InformacoesComplementares
        fields = (
            'paciente',
            'escola',
            'serie',
            'turno',
            'gravidez',
            'fatos_marcantes',
            'condicoes_emocionais',
            'pos_parto',
            'parto',
            'semanas',
            'peso',
            'altura',
            'cuidados_parto',
            'apgar1',
            'apgar5',
            'succao',
            'leite_marterno',
            'usou_mamadeira',
            'alimento_atual',
            'come_sem_derramar',
            'recebe_ajuda',
            'sono',
            'baba',
            'acorda',
            'fala_dormindo',
            'dorme_sozinho',
            'horario_de_dormir',
            'esfincteres',
            'fobias',
            'mora',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'
