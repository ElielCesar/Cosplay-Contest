from django.urls import path
from .views import *

app_name = 'autenticacao'

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name='logout'),
]
    