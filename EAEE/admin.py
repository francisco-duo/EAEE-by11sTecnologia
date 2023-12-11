from django.contrib import admin

from .models import PacienteModel, PacienteRegistroModel, RegistroFinanceiroTipoModel

# Register your models here.
admin.site.register(PacienteModel)
admin.site.register(PacienteRegistroModel)
admin.site.register(RegistroFinanceiroTipoModel)