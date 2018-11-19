from django.urls import path

from . import views

app_name = 'checkout'
urlpatterns = [
    path('carrinho/adicionar/<slug:slug>/', views.create_cart_item, name='create_cart_item'),
    path('carrinho/', views.cart_item,  name='cart_item'),
    path('finalizando/', views.checkout, name='checkout'),
    path('finalizando/<int:pk>/pagseguro', views.pagseguro_view, name='pagseguro_view'),
    path('notificacoes/pagseguro/', views.pagseguro_notification, name='pagseguro_notification')
]