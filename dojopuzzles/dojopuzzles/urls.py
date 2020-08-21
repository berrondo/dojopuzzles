# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from problemas.models import ProblemaUtilizado

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^problemas/', include('problemas.urls')),
    (r'^contribuicoes/', include('contribuicoes.urls')),

    url(r'^$', TemplateView.as_view(template_name='index.html'),
    #      'extra_context': {'problemas_utilizados': ProblemaUtilizado.objects.count}},
        
         name='inicio'),
    url(r'^sobre/$', TemplateView.as_view(template_name='sobre.html'), 
    # extra_context={'titulo_pagina': 'Sobre'}),
        name='sobre'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
