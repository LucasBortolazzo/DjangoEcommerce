from django.shortcuts import render

from .models import Product, Category
from django.db import connection

def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }

    return render(request, 'catalog/product_list.html', context)   

def category(request, slug):
    categoria = Category.objects.get(slug=slug)

    #Product.objects.filter(category__slug=slug)  filter by fk
    print(connection.queries)
    context = {
       'current_category': categoria.name,
       'product_list': Product.objects.filter(category=categoria.id) 
    }
    return render(request, 'catalog/category.html', context)      
  
def productdetail(request, slug):
    produto = Product.objects.get(slug=slug)

    context = {
        'product': produto
    }  

    return render(request, 'catalog/product.html', context)