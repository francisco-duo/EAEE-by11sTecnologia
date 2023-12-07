from django.urls import path
from .views import home_page, app_login, user_page, patient_register, patient_view,patient_search_view, register_patients_sessions

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', app_login, name='login'),
    path('usuario/inicio', user_page, name='access'),
    path('usuario/cadastro', patient_register, name='patient_register'),
    path('usuario/pacientes', patient_view, name='patient_view'),
    path('usuario/registros', register_patients_sessions, name='register_patients_sessions'),
    path('usuario/pacientes/busca', patient_search_view, name='patient_search_view'),
]
