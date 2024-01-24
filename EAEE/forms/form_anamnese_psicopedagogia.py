from django import forms
from EAEE.models import Psicopedagogia


class PsicopedagogiaForm(forms.ModelForm):

    class Meta:
        model = Psicopedagogia
        fields = (
            'especialista',
            'paciente',
            'idade_que_comecou_a_frequentar_escola',
            'como_foi_adaptacao',
            'reprovou',
            'ralacao_professores_colegas',
            'motivado_escola',
            'falta_assiduo',
            'realiza_atividades_com_satisfacao',
            'precisa_ajuda',
            'predilecao_matematica_portugues',
            'dificuldades_aprendizagem',
            'antecedentes_com_dificuldade',
            'queixas_comuns_escola',
            'fala_compreensivel',
            'corporalmente_desenvolto',
            'anda_bicicleta',
            'organizado',
            'ajuda_em_casa',
            'censurado',
            'brinquedos_favorito',
            'gosta_desenhar',
            'uso_de_eletronicos',
            'horas_livres',
            'potencialidades_marcantes',
            'fragilidades_evidentes',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'
