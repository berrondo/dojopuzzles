#!-*- coding: utf-8 -*-
from django.conf.urls import *
from contribuicoes.views import contribuicao, contribuicao_recebida

urlpatterns = [
    url(r'^contribua/$', contribuicao, name='contribua'),
    url(r'^recebida/$', contribuicao_recebida, name='contribuicao-recebida'),
]
