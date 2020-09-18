from .models import Category

def categories(request):
    return {
        'categorias': Category.objects.all()
    }    