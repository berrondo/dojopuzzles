# -*- coding: utf-8 -*-
from django.urls import include, path, re_path as url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from dojopuzzles.views import index, sobre

urlpatterns = [
    url(r'^problemas/', include('problemas.urls')),
    url(r'^contribuicoes/', include('contribuicoes.urls')),

    url(r'^$', index, name='inicio'),
    url(r'^sobre/$', sobre, name='sobre'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
]
