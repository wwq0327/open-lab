from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url(r'^$', 'tags.views.all_tags', name='all_tags'),
                       url(r'^(?P<tag>[^/]+)/$', 'tags.views.prj_tag', name="prj_tag"),
                       url(r'^(?P<tag>[^/]+)/u/(?P<username>\w+)/$', 'tags.views.prj_user_tag', name="prj_user_tag"),
)
