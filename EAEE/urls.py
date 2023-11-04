from django.urls import path
from .views import home_page, app_login

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', app_login, name='login'),
]