from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('payment/<int:order_id>/', views.payment, name='payment'),
    path('success/<int:order_id>/', views.success, name='success'),
    path('failed/', views.failed, name='failed'),
    path('history/', views.order_history, name='order_history'),
]
