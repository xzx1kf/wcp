
from django.conf.urls import patterns, include, url
from prediction import views

urlpatterns = patterns('',
    url(r'^$', views.predictions, name='predictions'),
)
