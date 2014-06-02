from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^portal/', include('portal.urls')),
  url(r'^predictions/', include('prediction.urls')),

  # admin page
  url(r'^admin/', include(admin.site.urls)),
)
