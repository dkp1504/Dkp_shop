from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.index, name='product_list'),
    # path('shop/', views.shop, name='shop_list'),
    path('products/<slug:slug>/', views.product_details, name='product_details'),
]
