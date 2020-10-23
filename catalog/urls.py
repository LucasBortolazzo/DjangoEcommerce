from django.contrib import admin
from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('categoria/<slug:slug>/', views.category, name='category'),
    path('produto/<slug:slug>/', views.productdetail, name='productdetail')
]