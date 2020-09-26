from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('contato/', views.contact, name='contact'),
    path('produto/', views.product, name='product'),
]
