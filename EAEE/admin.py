from django.contrib import admin

from .models import PacienteModel, PacienteRegistroModel

# Register your models here.
admin.site.register(PacienteModel)
admin.site.register(PacienteRegistroModel)