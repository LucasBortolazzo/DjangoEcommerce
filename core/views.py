from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category
from .forms import ContactForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def product(request):
    return render(request, 'product.html')       