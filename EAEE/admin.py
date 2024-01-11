from django.contrib import admin
from EAEE.models import *


class PacienteModelAdmin(admin.ModelAdmin):
    list_display = ('paciente_nome', 'paciente_dt_nascimento', )
    search_fields = ['paciente_nome', ]


class ResponsavelAdmin(admin.ModelAdmin):
    list_display = (
        'paciente_filiacao_nome',
        'paciente_filiacao_tipo_vinculo',
        'paciente_filiacao_email',
        'paciente_filiacao_dt_nascimento',
        'paciente_filiacao_contato_telefone_pessoal',
        'paciente_filiacao_cpf',
        'paciente_filiacao_estado_civil',
        'paceinte_filiacao_endereco',
        'paceinte_filiacao_cep',
    )
    search_fields = ['paciente_filiacao_nome',]


class AgendamentoAdmin(admin.ModelAdmin):
    list_display = (
        'paciente',
        'especialidade',
        'dt_agendamento',
        'presente',
        'falta',
        'reposicao',
        'justificativa',
    )
    list_editable = (
        'presente',
        'falta',
        'reposicao',
        'justificativa',
    )


class DevolutivaAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'dt_devolutiva'
    )
    search_fields = ['paciente',]


class ReuniaoExternaAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'dt_devolutiva'
    )
    search_fields = ['paciente',]


class EncaminhamentoAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'dt_devolutiva'
    )
    search_fields = ['paciente',]


class EvolucaoDiariaAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'dt_devolutiva'
    )
    search_fields = ['paciente',]


admin.site.register(PacienteModel, PacienteModelAdmin)
admin.site.register(TipoDeVinculoComPacienteModels, ResponsavelAdmin)
admin.site.register(InformacoesComplementares)
admin.site.register(RegistroFinanceiroModel)
admin.site.register(RegistroFinanceiroTipoModel)

admin.site.register(Devolutiva, DevolutivaAdmin)
admin.site.register(ReunioesExternas, ReuniaoExternaAdmin)
admin.site.register(Encaminhamento, EncaminhamentoAdmin)
admin.site.register(EvolucaoDiaria, EvolucaoDiariaAdmin)


admin.site.register(Agendamento, AgendamentoAdmin)
