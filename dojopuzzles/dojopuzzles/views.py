from django.shortcuts import render
from problemas.models import ProblemaUtilizado


def index(request):
    problemas_utilizados = ProblemaUtilizado.objects.count
    return render(request, 'index.html', locals())


def sobre(request):
    titulo_pagina = 'Sobre'
    return render(request, 'sobre.html', locals())