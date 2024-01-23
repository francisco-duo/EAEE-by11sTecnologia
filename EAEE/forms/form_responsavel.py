from django import forms
from EAEE.models import TipoDeVinculoComPacienteModels


class ResponsavelForm(forms.ModelForm):

    class Meta:
        model = TipoDeVinculoComPacienteModels
        fields = (
            'paciente', 'paciente_filiacao_nome',
            'paciente_filiacao_tipo_vinculo', 'paciente_filiacao_email',
            'paciente_filiacao_dt_nascimento', 'paciente_filiacao_contato_telefone_pessoal',
            'paciente_filiacao_contato_telefone_empresa', 'paciente_filiacao_cpf',
            'paciente_filiacao_nacionalidade', 'paciente_filiacao_profissao',
            'paciente_filiacao_estado_civil', 'paceinte_filiacao_endereco',
            'paceinte_filiacao_cep', 'paceinte_filiacao_comprovante_residencia',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'
            