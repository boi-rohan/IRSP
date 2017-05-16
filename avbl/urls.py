from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    # avbl/
    url(r'^$', views.index, name = 'index'),

    # avbl/<court_id>/
    url(r'^(?P<court_id>[0-9]+)/$', views.detail, name = 'detail'),
]
