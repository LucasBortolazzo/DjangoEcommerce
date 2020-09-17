from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('product_list/', views.product_list, name='product_list'),
    path('products/', views.products, name='products'),
]
