from django.shortcuts import render

# Create your views here.

from lucarsblog.models import *

def mostrar_lucarsblog(request):

    F1=automovil(marca='Ferrari', modelo='458')
    F2=automovil(marca='Porsche', modelo='911')
    F3=automovil(marca='Lamborghini', modelo='Aventador')

    return render(request, 'lucarsblog/lucarsblog.html', {'lucarsblog':[F1,F2,F3]})
    