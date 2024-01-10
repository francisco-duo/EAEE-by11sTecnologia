from django.contrib import admin
from EAEE.models import *


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

admin.site.register(DevolutivaModel, DevolutivaAdmin)
admin.site.register(ReunioesExternasModel, ReuniaoExternaAdmin)
admin.site.register(EncaminhamentoModel, EncaminhamentoAdmin)
admin.site.register(EvolucaoDiariaModel, EvolucaoDiariaAdmin)
