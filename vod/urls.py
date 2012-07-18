from django.conf.urls.defaults import *
from vod import settings
from view import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^vod/', include('vod.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    ('^$', index),
    ('^c/$', c),
    ('^nowplaying/$', nowplaying),
)
