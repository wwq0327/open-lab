from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^comments/', include('django.contrib.comments.urls')),
                       url(r'^ckeditor/', include('ckeditor.urls')),
                       url(r'^demo/$', include('demo.urls')),
                       url(r'^accounts/', include('profiles.urls')),
                       url(r'^$', include('home.urls')),
                       #url(r'^works/', include('works.urls')),
                       url(r'^projects/', include('projects.urls')),
)

urlpatterns += patterns('',

)


media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
urlpatterns += patterns('',
                        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
                         {
                             'document_root': settings.MEDIA_ROOT,
                             }),
                        )
