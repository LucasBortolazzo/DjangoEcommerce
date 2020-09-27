from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Category
from django.db import connection


class ProductListView(generic.ListView):
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.all()
    paginate_by = 2
    #model = Product


product_list = ProductListView.as_view()    
        

'''
def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }

    return render(request, 'catalog/product_list.html', context)   
'''
class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html' 
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs) 
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug']) 
        return context       

category = CategoryListView.as_view()
            


'''
def category(request, slug):
    categoria = Category.objects.get(slug=slug)

    #Product.objects.filter(category__slug=slug)  filter by fk
    print(connection.queries)
    context = {
       'current_category': categoria.name,
       'product_list': Product.objects.filter(category=categoria.id) 
    }
    return render(request, 'catalog/category.html', context)    

'''      
  
def productdetail(request, slug):
    produto = Product.objects.get(slug=slug)

    context = {
        'product': produto
    }  

    return render(request, 'catalog/product.html', context)   