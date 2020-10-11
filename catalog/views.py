from django.shortcuts import render, get_object_or_404
from django.views import generic
from model_mommy import mommy

from .models import Product, Category
from django.db import connection


class ProductListView(generic.ListView):

    #mommy.make('catalog.Product', _quantity= 100)

    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 2
    queryset = Product.objects.all()
    print(f'query:  {queryset.query}')
    #model = Product


product_list = ProductListView.as_view()    
        
class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html' 
    context_object_name = 'product_list'
    paginate_by = 10

    def get_queryset(self):
        produto = Product.objects.filter(category__slug=self.kwargs['slug'])
        print(produto.query)
        return produto

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs) 
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug']) 
        return context       

category = CategoryListView.as_view()
              
  
def productdetail(request, slug):
    produto = Product.objects.get(slug=slug)

    context = {
        'product': produto
    }  

    return render(request, 'catalog/product.html', context)   


'''
def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }

    return render(request, 'catalog/product_list.html', context)   
'''

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