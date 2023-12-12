from .home_views import home_page
from .login_views import app_login
from .register_views import cadastrar_usuario
from .user_view import (
    user_page, patient_register, patient_view,
    register_patients_sessions, patient_search_view,
    patient_session_view, patient_session_search_view,
    financeiro, financeiro_search
)
from .pdf_generator_view import render_pdf_view, render_pdf_session
