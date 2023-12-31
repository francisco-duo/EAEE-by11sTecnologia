from django.urls import path
from . import views


urlpatterns = [
    path('', views.teste, name='site'),
    path('login/', views.app_login, name='login'),
    path('inicio/<str:usuario>/', views.inicio, name='inicio'),
    path('inicio/<str:usuario>/comunicado/<int:pk>', views.visualizar_comunicado, name='visualizar_comunicado'),
    path('inicio/<str:usuario>/registro_fonoaudiologia', views.registro_fonoaudiologia, name='registro_fonoaudiologia'),
    path('inicio/<str:usuario>/registro_fonoaudiologia/<int:pk>', views.registro_fonoaudiologia_visualizar, name='registro_fonoaudiologia_visualizar'),
    path('inicio/<str:usuario>/registro_psicologia', views.registro_psicologia, name='registro_psicologia'),
    path('inicio/<str:usuario>/registro_psicomotricidade', views.registro_psicomotricidade, name='registro_psicomotricidade'),
    path('inicio/<str:usuario>/registro_psicopedagogia', views.registro_psicopedagogia, name='registro_psicopedagogia'),
    path('inicio/<str:usuario>/financeiro', views.financeiro, name='financeiro'),
    path('inicio/<str:usuario>/financeiro-busca', views.financeiro_search, name='financeiro_busca'),
    path('inicio/<str:usuario>/enviar-mensagem', views.enviar_mensagem, name='enviar_mensagem'),
    # path('inicio/<str:usuario>/visualizar-mensagem', views.visualizar_comunicado, name='visualizar_comunicado'),
    path('inicio/<str:usuario>/cadastro-usuario', views.cadastrar_usuario, name='cadastro_usuario'),
    path('inicio/<str:usuario>/cadastro-usuario/permissoes', views.cadastrar_usuario_permissoes, name='cadastrar_usuario_permissoes'),
    path('inicio/<str:usuario>/cadastro-de-paciente', views.cadastrar_novo_paciente, name='cadastrar_paciente'),
    path('inicio/<str:usuario>/cadastro-de-paciente/pacientes', views.pacientes, name='pacientes'),
    path('inicio/<str:usuario>/cadastro-de-paciente/pacientes/<int:pk>', views.pacientes_visualizar, name='pacientes_visualizar'),
    path('inicio/<str:usuario>/cadastro-de-paciente/busca', views.pacientes_busca, name='pacientes_busca'),
    path('inicio/<str:usuario>/cadastro-de-paciente/cadastro-responsavel', views.cadastrar_responsavel, name='cadastrar_responsavel'),
    path('inicio/<str:usuario>/anamnese/anamnese_psicopedagogia', views.anamnese_psicopedagogia, name='anamnese_psicopedagogia'),
    path('inicio/<str:usuario>/anamnese/anamnese_psicologia', views.anamnese_psicologia, name='anamnese_psicologia'),
    path('inicio/<str:usuario>/anamnese/anamnese_fonoaudiologia', views.anamnese_fonoaudiologia, name='anamnese_fonoaudiologia'),
    path('inicio/<str:usuario>/anamnese/anamnese_psicomotricidade', views.anamnese_psicomotricidade, name='anamnese_psicomotricidade'),
    path('inicio/<str:usuario>/pdi/devolutiva', views.devolutiva, name='devolutiva'),
    path('inicio/<str:usuario>/pdi/reunioes_externas', views.reunioes_externas, name='reunioes_externas'),
    path('inicio/<str:usuario>/pdi/encaminhamento', views.encaminhamento, name='encaminhamento'),
    path('inicio/<str:usuario>/pdi/evolucao_diaria', views.evolucao_diaria, name='evolucao_diaria'),
    path('inicio/<str:usuario>/pdi/supervisao_multiprofissional', views.supervisao_multiprofissional, name='supervisao_multiprofissional'),

    # path('', home_page, name='home'),
    # path('login/', app_login, name='login'),
    # path('usuario/cadastrar', cadastrar_usuario, name='cadastro'),
    # path('usuario/inicio', user_page, name='access'),
    # path('usuario/cadastro', patient_register, name='patient_register'),
    # path('usuario/pacientes', patient_view, name='patient_view'),
    # path('usuario/pacientes/editar/<int:pk>', patient_edit, name='patient_edit'),
    # path('usuario/registros', register_patients_sessions, name='register_patients_sessions'),
    # path('usuario/registros_usuario', patient_session_view, name='patient_session_view'),
    # path('usuario/registros_usuario/busca', patient_session_search_view, name='patient_session_search_view'),
    # path('usuario/registros_usuario/pdf/<int:pk>', render_pdf_view, name='pdf_view'),
    # path('usuario/registros_usuario/pdf/registro/<int:pk>', render_pdf_session, name='pdf_view_session'),
    # path('usuario/pacientes/busca', patient_search_view, name='patient_search_view'),
    # path('usuario/financeiro', financeiro, name='financeiro'),
    # path('usuario/financeiro/busca', financeiro_search, name='financeiro_search'),
]
