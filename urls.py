from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^garden_path/', include('garden_path.foo.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^garden_path/index', 'paths.views.index'),
    (r'^garden_path/(?P<path_nick>\w+)/$', 'paths.views.detail'),
    (r'^static_media/(?P<path>.*)$', 'django.views.static.serve', \
      {'document_root': settings.STATIC_DOC_ROOT})
)
