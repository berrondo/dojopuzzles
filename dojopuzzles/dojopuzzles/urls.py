# -*- coding: utf-8 -*-
from django.urls import include, path, re_path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from dojopuzzles.views import index, sobre

urlpatterns = [
    re_path(r'^problemas/', include('problemas.urls')),
    re_path(r'^contribuicoes/', include('contribuicoes.urls')),

    re_path(r'^$', index, name='inicio'),
    re_path(r'^sobre/$', sobre, name='sobre'),

    # Uncomment the admin/doc line below to enable admin documentation:
    re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    re_path(r'^admin/', admin.site.urls),
]
