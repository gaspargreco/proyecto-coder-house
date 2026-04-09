from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import DepartamentosMedicos
# Create your views here.
#def inicio(request):
    #return render(request, "inicio/index.html")


def inicio(request):
    return render(request, "inicio/index.html",{})

def prueba_bucle(request):
    
    numeros = list(range(1, 11))
    
    return render(request, "inicio/prueba_bucle.html", )