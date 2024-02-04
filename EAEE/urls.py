from django.urls import path
from . import views


urlpatterns = [
    path('', views.teste, name='site'),
    path('login/', views.app_login, name='login'),
    path('inicio/<str:usuario>/', views.inicio, name='inicio'),
    path('inicio/<str:usuario>/comunicado/<int:pk>',
         views.visualizar_comunicado, name='visualizar_comunicado'),

    # FINANCEIRO
    path('inicio/<str:usuario>/financeiro',
         views.financeiro, name='financeiro'),
    path('inicio/<str:usuario>/financeiro-busca',
         views.financeiro_search, name='financeiro_busca'),

    # MENSAGEM
    path('inicio/<str:usuario>/enviar-mensagem',
         views.enviar_mensagem, name='enviar_mensagem'),

    # PACIENTES E RESPONSAVEIS
    path('inicio/<str:usuario>/cadastro-de-paciente',
         views.cadastrar_novo_paciente, name='cadastrar_paciente'),
    path('inicio/<str:usuario>/cadastro-de-paciente/pacientes',
         views.pacientes, name='pacientes'),
    path('inicio/<str:usuario>/cadastro-de-paciente/pacientes/<int:pk>',
         views.pacientes_visualizar, name='pacientes_visualizar'),
    path('inicio/<str:usuario>/cadastro-de-paciente/busca',
         views.pacientes_busca, name='pacientes_busca'),
    path('inicio/<str:usuario>/cadastro-responsavel',
         views.cadastrar_responsavel, name='cadastrar_responsavel'),
    path('inicio/<str:usuario>/responsaveis',
         views.responsaveis, name='responsaveis'),
    path('inicio/<str:usuario>/responsaveis/<int:pk>',
         views.responsavel_visualizar, name='responsaveis_visualizar'),
    path('inicio/<str:usuario>/informacoes-coplementares',
         views.paciente_inforacoes_complementares,
         name='paciente_inforacoes_complementares'),

    # ANAMNESES
    # psicopedagogia
    path('inicio/<str:usuario>/anamnese/anamnese_psicopedagogia',
         views.form_anamnese_psicopedagogia,
         name='form_anamnese_psicopedagogia'),
    path('inicio/<str:usuario>/anamnese/anamneses_psicopedagogia',
         views.list_anamnese_psicopedagogia,
         name='list_anamnese_psicopedagogia'),
    path('inicio/<str:usuario>/anamnese/anamnese_psicopedagogia/<int:pk>',
         views.edit_anamnese_psicopedagogia,
         name='edit_anamnese_psicopedagogia'),
    path('inicio/<str:usuario>/anamnese/anamnese_psicopedagogia/search',
         views.search_anamnese_psicopedagogia,
         name='search_anamnese_psicopedagogia'),

    # ANAMNESES
    # fonoaudiologia
    path('inicio/<str:usuario>/anamnese/anamnese_fonoaudiologia',
         views.form_anamnese_fonoaudiologia,
         name='form_anamnese_fonoaudiologia'),
    path('inicio/<str:usuario>/anamnese/registro_anamnese_fonoaudiologia',
         views.list_anamnese_fonoaudiologia,
         name='list_anamnese_fonoaudiologia'),
    path('inicio/<str:usuario>/anamnese/anamnese_fonoaudiologia/<int:pk>',
         views.edit_anamnese_fonoaudiologia,
         name='edit_anamnese_fonoaudiologia'),
    path('inicio/<str:usuario>/anamnese/anamnese_fonoaudiologia/search',
         views.search_anamnese_fonoaudiologia,
         name='search_anamnese_fonoaudiologia'),

    # ANAMNESES
    # psicologia
    path('inicio/<str:usuario>/anamnese/anamnese_psicologia',
         views.form_anamnese_psicologia,
         name='form_anamnese_psicologia'),
    path('inicio/<str:usuario>/anamnese/registro_anamnese_psicologia',
         views.list_anamnese_psicologia,
         name='list_anamnese_psicologia'),
    path('inicio/<str:usuario>/anamnese/anamnese_psicologia/<int:pk>',
         views.edit_anamnese_psicologia,
         name='edit_anamnese_psicologia'),
    path('inicio/<str:usuario>/anamnese/anamnese_psicologia/search',
         views.search_anamnese_psicologia,
         name='search_anamnese_psicologia'),

    # ANAMNESES
    # psicomotricidade
    path('inicio/<str:usuario>/anamnese/anamnese_psicomotricidade',
         views.form_anamnese_psicomotricidade,
         name='form_anamnese_psicomotricidade'),
    path('inicio/<str:usuario>/anamnese/anamneses_psicomotricidade',
         views.list_anamnese_psicomotricidade,
         name='list_anamnese_psicomotricidade'),
    path('inicio/<str:usuario>/anamnese/anamnese_psicomotricidade/<int:pk>',
         views.edit_anamnese_psicomotricidade,
         name='edit_anamnese_psicomotricidade'),
    path('inicio/<str:usuario>/anamnese/anamnese_psicomotricidade/search',
         views.search_anamnese_psicomotricidade,
         name='search_anamnese_psicomotricidade'),
    
    # ANAMNESES
    # terapia_ocupacional
    path('inicio/<str:usuario>/anamnese/anamnese_terapia_ocupacional',
         views.form_anamnese_terapia_ocupacional,
         name='form_anamnese_terapia_ocupacional'),
    path('inicio/<str:usuario>/anamnese/anamneses_terapia_ocupacional',
         views.list_anamnese_terapia_ocupacional,
         name='list_anamnese_terapia_ocupacional'),
    path('inicio/<str:usuario>/anamnese/anamnese_terapia_ocupacional/<int:pk>',
         views.edit_anamnese_terapia_ocupacional,
         name='edit_anamnese_terapia_ocupacional'),
    path('inicio/<str:usuario>/anamnese/anamnese_terapia_ocupacional/search',
         views.search_anamnese_terapia_ocupacional,
         name='search_anamnese_terapia_ocupacional'),

    path('inicio/<str:usuario>/pdi/devolutiva',
         views.devolutiva, name='devolutiva'),
    path('inicio/<str:usuario>/pdi/devolutivas',
         views.devolutivas, name='devolutivas'),
    path('inicio/<str:usuario>/pdi/devolutiva/<int:pk>',
         views.devolutiva_visualizar, name='devolutiva_visualizar'),
    path('inicio/<str:usuario>/pdi/reunioes_externas',
         views.reunioes_externas, name='reunioes_externas'),

    # ENCAMINHAMENTOS URLS
    path('inicio/<str:usuario>/encaminhamento',
         views.form_encaminhamento, name='view_encaminhamento'),
    path('inicio/<str:usuario>/encaminhamento/<int:pk>',
         views.edit_encaminhamento, name='edit_encaminhamento'),
    path('inicio/<str:usuario>/encaminhamentos',
         views.list_encaminhamento, name='list_encaminhamento'),
    path('inicio/<str:usuario>/encaminhamento/search',
         views.search_encaminhamento, name='search_encaminhamento'),

    # EVOLUÇÃO DIÁRIA
    path('inicio/<str:usuario>/evolucao_diaria',
         views.form_evolucao_diaria, name='form_evolucao_diaria'),
    path('inicio/<str:usuario>/evolucoes_diarias',
         views.list_evolucao_diaria, name='list_evolucao_diaria'),
    path('inicio/<str:usuario>/evolucao_diaria/<int:pk>',
         views.edit_evolucao_diaria, name='edit_evolucao_diaria'),
    path('inicio/<str:usuario>/evolucao_diaria/search',
         views.search_evolucao_diaria, name='search_evolucao_diaria'),

    # REUNIÕES EXTERNAS
    path('inicio/<str:usuario>/reuniao_externa',
         views.form_reunioes_externas, name='form_evolucao_diaria'),
    path('inicio/<str:usuario>/reunioes_externas',
         views.list_reunioes_externas, name='list_reunioes_externas'),
    path('inicio/<str:usuario>/reunioes_externas/<int:pk>',
         views.edit_reunioes_externas, name='edit_reunioes_externas'),
    path('inicio/<str:usuario>/reunioes_externas/search',
         views.search_reunioes_externas, name='search_reunioes_externas'),

    # SUPERVISÃO MULTIDISCIPLINAR
    path('inicio/<str:usuario>/supervisao_multidisciplinar',
         views.form_supervisao_multidisciplinar,
         name='form_supervisao_multidisciplinar'),
    path('inicio/<str:usuario>/supervisoes_multidisciplinares',
         views.list_supervisao_multidisciplinar,
         name='list_supervisao_multidisciplinar'),
    path('inicio/<str:usuario>/supervisao_multidisciplinar/<int:pk>',
         views.edit_supervisao_multidisciplinar,
         name='edit_supervisao_multidisciplinar'),
    path('inicio/<str:usuario>/supervisao_multidisciplinar/search',
         views.search_supervisao_multidisciplinar,
         name='search_supervisao_multidisciplinar'),

    path('inicio/<str:usuario>/pdi/supervisao_multiprofissional',
         views.supervisao_multiprofissional,
         name='supervisao_multiprofissional')
]
