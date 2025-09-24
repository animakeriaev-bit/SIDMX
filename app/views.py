from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def principal(request):
    return render(request,'home.html',{})

def servicios(request):
    return render(request,'servicios.html',{})

def portafolio(request):
    return render(request, 'portafolio.html', {})

def nosotros(request):
    return render(request, 'nosotros.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def construccion(request):
    return render(request, 'construccion.html', {})

def remodelacion(request):
    return render(request, 'remodelacion.html',{})

def mantenimiento(request):
    return render(request, 'mantenimiento.html', {})

def gestion(request):
    return render(request,'gestion.html', {})