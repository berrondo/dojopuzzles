#!-*- coding: utf-8 -*-
from django.conf.urls import *

from problemas.models import Problema
from problemas.views import ListaTodosOsProblemas

urlpatterns = patterns('',
    url(r'^$', 'problemas.views.problema_aleatorio', name='problema-aleatorio'),
    url(r'^exibe/(?P<slug>[\w_-]+)/$', 'problemas.views.exibe_problema', name='exibe-problema'),

    url(r'^busca/$', 'problemas.views.busca_problema_por_titulo', 
            name='busca-problema-por-titulo'),

    url(r'^(?P<problema_id>\d+)/$', 'problemas.views.exibe_problema_pelo_id', name='exibe-problema-pelo-id'),
    url(r'^gostei/(?P<problema_id>\d+)/$', 'problemas.views.problema_utilizado', name='problema-utilizado-em-dojo'),
    url(r'^todos_visualizados/$', 'problemas.views.sem_problemas_novos', name='sem-problemas-novos'),
    url(r'^nenhum_problema/$', 'problemas.views.sem_problemas', name='nenhum-problema-cadastrado'),

    url(r'^todos/$', ListaTodosOsProblemas.as_view(template_name='problema_list.html'),
         name='todos-problemas'),
)
