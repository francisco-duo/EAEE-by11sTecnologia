from django.contrib import admin
from EAEE.models import *


admin.site.register(PermissoesModel)
# from .models import PacienteModel, PacienteRegistroModel, RegistroFinanceiroTipoModel

# # Register your models here.
# admin.site.register(PacienteModel)
admin.site.register(RegistroFinanceiroModel)
admin.site.register(RegistroFinanceiroTipoModel)
admin.site.register(PacienteModel)
admin.site.register(TipoDeVinculoComPacienteModels)
admin.site.register(DevolutivaModel)
admin.site.register(ReunioesExternasModel)
admin.site.register(EncaminhamentoModel)
admin.site.register(EvolucaoDiariaModel)