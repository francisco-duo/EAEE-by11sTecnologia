from django.contrib import admin
from EAEE.models import PermissoesModel, RegistroFinanceiroTipoModel, RegistroFinanceiroModel

admin.site.register(PermissoesModel)
# from .models import PacienteModel, PacienteRegistroModel, RegistroFinanceiroTipoModel

# # Register your models here.
# admin.site.register(PacienteModel)
admin.site.register(RegistroFinanceiroModel)
admin.site.register(RegistroFinanceiroTipoModel)