# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url(r'^$', 'works.views.index', name="ws_index"),
                       url(r'^create/$', 'works.views.ws_create', name="ws_create"),
                       url(r'^(?P<ws_pk>\d+)/$', 'works.views.ws_page', name="ws_page"),
)
