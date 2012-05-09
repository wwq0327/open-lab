from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url(r'^$', 'demo.views.index'),
)
