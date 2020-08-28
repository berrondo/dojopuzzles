#!-*- coding: utf-8 -*-
from django.conf.urls import *

from problemas.models import Problema
from problemas.views import *

urlpatterns = [
    url(r'^$', problema_aleatorio, name='problema-aleatorio'),
    url(r'^exibe/(?P<slug>[\w_-]+)/$', exibe_problema, name='exibe-problema'),
    url(r'^busca/$', busca_problema_por_titulo, name='busca-problema-por-titulo'),
    url(r'^(?P<problema_id>\d+)/$', exibe_problema_pelo_id, name='exibe-problema-pelo-id'),
    url(r'^gostei/(?P<problema_id>\d+)/$', problema_utilizado, name='problema-utilizado-em-dojo'),
    url(r'^todos_visualizados/$', sem_problemas_novos, name='sem-problemas-novos'),
    url(r'^nenhum_problema/$', sem_problemas, name='nenhum-problema-cadastrado'),
    url(r'^todos/$', ListaTodosOsProblemas.as_view(), name='todos-problemas'),
]
