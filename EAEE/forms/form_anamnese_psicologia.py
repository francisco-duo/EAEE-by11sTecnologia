from django import forms
from EAEE.models import Psicologia


class PsicologiaForm(forms.ModelForm):

    class Meta:
        model = Psicologia
        fields = (
            'especialista',
            'paciente',
            'numero_irmaos',
            'reacao_nascimento_irmao',
            'relacionamento_irmaos',
            'relacionamento_pais',
            'relacionamento_familia',
            'personalidade',
            'comportamento_roer_unhas',
            'humor_habitual',
            'brinca_sozinho_ou_grupo',
            'estranha_mudancas_ambiente',
            'aceita_seguir_comandos',
            'brincadeiras_brinquedo_favorito',
            'gosta_de_musicas',
            'baste_cabeca_na_parede',
            'atitudes_desse_habito',
            'reprovou_na_escola',
            'relacionamento_colegas',
            'relacionamento_professores',
            'idade_desfralde',
            'dificuldades_desfraude',
            'higiene_sozinho',
            'idade_higiene_sozinho',
            'problema_na_fala',
            'troca_letras',
            'acorda_vai_para_cama_dos_pais',
            'dorme_sozinho',
            'objeto_para_dormir',
            'urina_na_cama',
            'horario_para_refeicoes',
            'refeicoes_em_familia',
            'local',
            'assiste_enquanto_come',
            'como_se_alimenta',
            'seletividade_alimentar',
            'curiosidade_sexual',
            'atitude_dos_pais',
            'informacoes_sexuais',
            'tratamento_medico',
            'internado',
            'motivo_internação',
            'operado',
            'idade_operado',
            'adoece_facilmente',
            'acompanhamento_psicologico',
            'encaminhamento',
            'algum_membro_ja_fez_acompanhamento_psicologico',
            'queixa_psicologica_principal',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'
