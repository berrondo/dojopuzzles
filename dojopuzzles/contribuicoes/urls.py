#!-*- coding: utf-8 -*-
from django.urls import re_path
from contribuicoes.views import contribuicao, contribuicao_recebida

urlpatterns = [
    re_path(r'^contribua/$', contribuicao, name='contribua'),
    re_path(r'^recebida/$', contribuicao_recebida, name='contribuicao-recebida'),
]
