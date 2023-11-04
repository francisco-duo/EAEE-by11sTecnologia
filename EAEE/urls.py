from django.urls import path
from .views import home_page, app_login, user_page

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', app_login, name='login'),
    path('usuario/<str:user_name>', user_page, name='access'),
]