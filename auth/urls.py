from django.conf.urls import patterns, include, url
from auth.views import *

urlpatterns = patterns('',
        (r'^$', main_page),
)
