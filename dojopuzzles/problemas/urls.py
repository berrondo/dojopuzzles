#!-*- coding: utf-8 -*-
from django.urls import *

from problemas.models import Problema
from problemas.views import *

urlpatterns = [
    re_path(r'^$', problema_aleatorio, name='problema-aleatorio'),
    re_path(r'^exibe/(?P<slug>[\w_-]+)/$', exibe_problema, name='exibe-problema'),
    re_path(r'^busca/$', busca_problema_por_titulo, name='busca-problema-por-titulo'),
    re_path(r'^(?P<problema_id>\d+)/$', exibe_problema_pelo_id, name='exibe-problema-pelo-id'),
    re_path(r'^gostei/(?P<problema_id>\d+)/$', problema_utilizado, name='problema-utilizado-em-dojo'),
    re_path(r'^todos_visualizados/$', sem_problemas_novos, name='sem-problemas-novos'),
    re_path(r'^nenhum_problema/$', sem_problemas, name='nenhum-problema-cadastrado'),
    re_path(r'^todos/$', ListaTodosOsProblemas.as_view(), name='todos-problemas'),
]
