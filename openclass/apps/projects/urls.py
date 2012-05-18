# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url(r'^$', 'projects.views.index', name="prj_index"),
                       url(r'^create/$', 'projects.views.prj_create', name="prj_create"),
                       url(r'^(?P<prj_pk>\d+)/$', 'projects.views.prj_page', name="prj_page"),
                       url(r'^(?P<prj_pk>\d+)/edit/$', 'projects.views.prj_edit', name="prj_edit"),
                       url(r'^(?P<prj_pk>\d+)/f/$', 'projects.views.prj_follow', name="prj_f"),
                       url(r'^(?P<prj_pk>\d+)/fd/$', 'projects.views.prj_follow_del', name="prj_fd"),
)
