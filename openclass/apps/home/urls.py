# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url(r'^$', 'home.views.index', name="h_index"), ## "{% url h_index %}" 全站首页
)
