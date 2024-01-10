from django.contrib import admin
from EAEE.models import *


class AgendamentoAdmin(admin.ModelAdmin):
    list_display = (
        'paciente',
        'especialidade',
        'dt_agendamento',
        'frequencia',
    )
    list_editable = ('frequencia',)


class DevolutivaAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'dt_devolutiva'
    )


class ReuniaoExternaAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'dt_devolutiva'
    )


class EncaminhamentoAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'dt_devolutiva'
    )


class EvolucaoDiariaAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'dt_devolutiva'
    )


admin.site.register(PacienteModel)
admin.site.register(TipoDeVinculoComPacienteModels)
admin.site.register(InformacoesComplementares)
admin.site.register(RegistroFinanceiroModel)
admin.site.register(RegistroFinanceiroTipoModel)

admin.site.register(Devolutiva, DevolutivaAdmin)
admin.site.register(ReunioesExternas, ReuniaoExternaAdmin)
admin.site.register(Encaminhamento, EncaminhamentoAdmin)
admin.site.register(EvolucaoDiaria, EvolucaoDiariaAdmin)


admin.site.register(Agendamento, AgendamentoAdmin)
