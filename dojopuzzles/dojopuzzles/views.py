from django.shortcuts import render_to_response
from django.template import RequestContext

from problemas.models import ProblemaUtilizado


def index(request):
    problemas_utilizados = ProblemaUtilizado.objects.count
    return render_to_response('index.html', locals(), RequestContext(request))


def sobre(request):
    titulo_pagina = 'Sobre'
    return render_to_response('sobre.html', locals(), RequestContext(request))