from django.shortcuts import render
from . models import PlacasMadre
from django.views import generic

# Create your views here.


def index(request):
    
    return render(
        request,
        'index.html',
        
    )

def placasmadres(request):
    num_producto = PlacasMadre.objects.all()

    return render(
        request,
        'placasmadres.html',
        context={'num_producto':num_producto},
    )
            
