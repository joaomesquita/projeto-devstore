from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('entrar/', LoginView.as_view(),  name='login'),
    path('sair/', LogoutView.as_view(), name='logout'),
    path('registro/', views.register, name='register'),
    path('alterar-dados/', views.update_user, name='update_user'),
    path('alterar-endereco/', views.update_address, name='update_address'),
    path('alterar-senha/', views.update_password, name='update_password'),
    path('recuperar-senha/', PasswordResetView.as_view(), name='password_reset'),
    path('recuperar-senha/enviado/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('recuperar-senha/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('recuperar-senha/completo/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('meus-pedidos/', views.order_list, name='order_list'),
    path('meus-pedidos/<int:pk>/', views.order_detail, name='order_detail')
]