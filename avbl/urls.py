from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    # avbl/
    url(r'^$', views.index, name = 'index'),

    # avbl/<court_id>/
    url(r'^(?P<court_id>[0-9]+)/$', views.detail, name = 'detail'),

    #avbl/apnd/<court_pk>/<time>/<rpi_data>
    url(r'^apnd/(?P<court_pk>[0-9]+)/(?P<time>[0-9]+)/(?P<rpi_data>[a-zA-Z]+)/$', views.apnd_table, name = 'apnd_table'),
]
