from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    path('produto/', views.product, name='product'),
    path('produtos/', views.products, name='products'),
]
