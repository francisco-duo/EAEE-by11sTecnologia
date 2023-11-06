from django.urls import path
from .views import home_page, app_login, user_page, patient_register, patient_view

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', app_login, name='login'),
    path('usuario/inicio', user_page, name='access'),
    path('usuario/cadastro', patient_register, name='patient_register'),
    path('usuario/pacientes', patient_view, name='patient_view'),
]