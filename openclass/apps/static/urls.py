# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url(r'^about/$', 'static.views.about', name="st_about"),
                       url(r'^contact/$', 'static.views.contact', name="st_contact"),
)
