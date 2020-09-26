from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category
from .forms import ContactForm
from django.views.generic import View, TemplateView

# Create your views here.

class index(TemplateView):
    template_name = 'index.html'   


def contact(request):
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def product(request):
    return render(request, 'product.html')       