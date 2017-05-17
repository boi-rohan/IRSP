from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    # avbl/
    url(r'^$', views.index, name = 'index'),

    # avbl/<court_id>/
    url(r'^(?P<court_id>[0-9]+)/$', views.detail, name = 'detail'),

    #avbl/apnd_<time>_<rpi_data>_<court_pk>/
    url(r'^apnd_(?P<time>[0-9]+)_(?P<rpi_data>[a-z]+)_(?P<court_pk>[0-9]+)/$', views.apnd_table, name = 'apnd_table'),
]
