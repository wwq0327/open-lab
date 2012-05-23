from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url(r'^$', 'events.views.index', name='events_index'),
)
