from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  url(r'^portal/', include('portal.urls')),
)
