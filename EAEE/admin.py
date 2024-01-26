from datetime import datetime
from django.contrib import admin
from EAEE.models import *


class PacienteModelAdmin(admin.ModelAdmin):
    list_display = ('paciente_nome', 'paciente_dt_nascimento', )
    search_fields = ['paciente_nome', ]
    ordering = ('paciente_nome', )


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
    ordering = ('paciente_filiacao_nome', )
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
    ordering = ('paciente', )
    search_fields = ['paciente__paciente_nome', 'dt_agendamento__month']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Tenta converter o termo de pesquisa para o nome do mês em inglês
        try:
            month_number = datetime.strptime(search_term, '%m').month
            month_name = datetime(2000, month_number, 1).strftime('%B')
            queryset |= self.model.objects.filter(dt_agendamento__month=month_number)
            queryset |= self.model.objects.filter(dt_agendamento__month=month_name)
        except ValueError:
            pass  # Se a conversão falhar, continue com a consulta padrão

        return queryset, use_distinct


class DevolutivaAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'dt_devolutiva'
    )
    search_fields = ['paciente__paciente_nome', 'dt_devolutiva__month', 'especialista__username']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Tenta converter o termo de pesquisa para o nome do mês em inglês
        try:
            month_number = datetime.strptime(search_term, '%m').month
            month_name = datetime(2000, month_number, 1).strftime('%B')
            queryset |= self.model.objects.filter(dt_devolutiva__month=month_number)
            queryset |= self.model.objects.filter(dt_devolutiva__month=month_name)
        except ValueError:
            pass  # Se a conversão falhar, continue com a consulta padrão

        return queryset, use_distinct


class SupervisaoMultiprofissionalAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'dt_devolutiva'
    )
    search_fields = ['paciente__paciente_nome', 'dt_devolutiva__month', 'especialista__username']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Tenta converter o termo de pesquisa para o nome do mês em inglês
        try:
            month_number = datetime.strptime(search_term, '%m').month
            month_name = datetime(2000, month_number, 1).strftime('%B')
            queryset |= self.model.objects.filter(dt_devolutiva__month=month_number)
            queryset |= self.model.objects.filter(dt_devolutiva__month=month_name)
        except ValueError:
            pass  # Se a conversão falhar, continue com a consulta padrão

        return queryset, use_distinct


class ReuniaoExternaAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'dt_devolutiva'
    )
    search_fields = ['paciente__paciente_nome', 'dt_devolutiva__month', 'especialista__username']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Tenta converter o termo de pesquisa para o nome do mês em inglês
        try:
            month_number = datetime.strptime(search_term, '%m').month
            month_name = datetime(2000, month_number, 1).strftime('%B')
            queryset |= self.model.objects.filter(dt_devolutiva__month=month_number)
            queryset |= self.model.objects.filter(dt_devolutiva__month=month_name)
        except ValueError:
            pass  # Se a conversão falhar, continue com a consulta padrão

        return queryset, use_distinct


class EncaminhamentoAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'dt_devolutiva'
    )
    search_fields = ['paciente__paciente_nome', 'dt_devolutiva__month', 'especialista__username']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Tenta converter o termo de pesquisa para o nome do mês em inglês
        try:
            month_number = datetime.strptime(search_term, '%m').month
            month_name = datetime(2000, month_number, 1).strftime('%B')
            queryset |= self.model.objects.filter(dt_devolutiva__month=month_number)
            queryset |= self.model.objects.filter(dt_devolutiva__month=month_name)
        except ValueError:
            pass  # Se a conversão falhar, continue com a consulta padrão

        return queryset, use_distinct


class EvolucaoDiariaAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'dt_devolutiva'
    )
    search_fields = ['paciente__paciente_nome', 'dt_devolutiva__month']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Tenta converter o termo de pesquisa para o nome do mês em inglês
        try:
            month_number = datetime.strptime(search_term, '%m').month
            month_name = datetime(2000, month_number, 1).strftime('%B')
            queryset |= self.model.objects.filter(dt_devolutiva__month=month_number)
            queryset |= self.model.objects.filter(dt_devolutiva__month=month_name)
        except ValueError:
            pass  # Se a conversão falhar, continue com a consulta padrão

        return queryset, use_distinct


class PsicopedagogiaAdmin(admin.ModelAdmin):
    list_display = (
        'especialista', 'paciente', 'dt_registro'
    )
    search_fields = (
        'especialista__username', 'paciente__paciente_nome',
        'dt_registro__month'
    )

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Tenta converter o termo de pesquisa para o nome do mês em inglês
        try:
            month_number = datetime.strptime(search_term, '%m').month
            month_name = datetime(2000, month_number, 1).strftime('%B')
            queryset |= self.model.objects.filter(dt_registro__month=month_number)
            queryset |= self.model.objects.filter(dt_registro__month=month_name)
        except ValueError:
            pass  # Se a conversão falhar, continue com a consulta padrão

        return queryset, use_distinct


class PsicologiaAdmin(admin.ModelAdmin):
    list_display = (
        'especialista', 'paciente', 'dt_registro'
    )
    search_fields = (
        'especialista__username', 'paciente__paciente_nome',
        'dt_registro__month'
    )

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Tenta converter o termo de pesquisa para o nome do mês em inglês
        try:
            month_number = datetime.strptime(search_term, '%m').month
            month_name = datetime(2000, month_number, 1).strftime('%B')
            queryset |= self.model.objects.filter(dt_registro__month=month_number)
            queryset |= self.model.objects.filter(dt_registro__month=month_name)
        except ValueError:
            pass  # Se a conversão falhar, continue com a consulta padrão

        return queryset, use_distinct


class PsicomotricidadeAdmin(admin.ModelAdmin):
    list_display = (
        'especialista', 'paciente', 'dt_registro'
    )
    search_fields = (
        'especialista__username', 'paciente__paciente_nome',
        'dt_registro__month'
    )

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Tenta converter o termo de pesquisa para o nome do mês em inglês
        try:
            month_number = datetime.strptime(search_term, '%m').month
            month_name = datetime(2000, month_number, 1).strftime('%B')
            queryset |= self.model.objects.filter(dt_registro__month=month_number)
            queryset |= self.model.objects.filter(dt_registro__month=month_name)
        except ValueError:
            pass  # Se a conversão falhar, continue com a consulta padrão

        return queryset, use_distinct


class FonoaudiologiaAdmin(admin.ModelAdmin):
    list_display = (
        'especialista', 'paciente', 'dt_registro'
    )
    search_fields = (
        'especialista__username', 'paciente__paciente_nome',
        'dt_registro__month'
    )

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Tenta converter o termo de pesquisa para o nome do mês em inglês
        try:
            month_number = datetime.strptime(search_term, '%m').month
            month_name = datetime(2000, month_number, 1).strftime('%B')
            queryset |= self.model.objects.filter(dt_registro__month=month_number)
            queryset |= self.model.objects.filter(dt_registro__month=month_name)
        except ValueError:
            pass  # Se a conversão falhar, continue com a consulta padrão

        return queryset, use_distinct


# admin.site.register(Psicopedagogia, PsicopedagogiaAdmin)
# admin.site.register(Psicologia, PsicologiaAdmin)
# admin.site.register(Psicomotricidade, PsicomotricidadeAdmin)
# admin.site.register(Fonoaudiologia, FonoaudiologiaAdmin)

admin.site.register(PacienteModel, PacienteModelAdmin)
admin.site.register(TipoDeVinculoComPacienteModels, ResponsavelAdmin)
# admin.site.register(InformacoesComplementares)
admin.site.register(RegistroFinanceiroModel)
admin.site.register(RegistroFinanceiroTipoModel)

admin.site.register(Devolutiva, DevolutivaAdmin)
admin.site.register(ReunioesExternas, ReuniaoExternaAdmin)
admin.site.register(Encaminhamento, EncaminhamentoAdmin)
admin.site.register(EvolucaoDiaria, EvolucaoDiariaAdmin)
admin.site.register(SupervisaoMultiprofissional, SupervisaoMultiprofissionalAdmin)


admin.site.register(Agendamento, AgendamentoAdmin)
