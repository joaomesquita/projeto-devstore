from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('entrar/', LoginView.as_view(),  name='login'),
    path('sair/', LogoutView.as_view(), name='logout'),
    path('registro/', views.register, name='register'),
    path('alterar-dados/', views.update_user, name='update_user'),
    path('alterar-endereco/', views.update_address, name='update_address'),
    path('alterar-senha/', views.update_password, name='update_password')
]