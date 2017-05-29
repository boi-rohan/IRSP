from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'avbl'
urlpatterns = [
    # avbl/
    url(r'^$', views.index, name = 'index'),

    # avbl/<court_id>/
    url(r'^(?P<court_id>[0-9]+)/$', views.detail, name = 'detail'),

    #avbl/apnd/<court_pk>/<date>/<time>/<rpi_data>
    url(r'^apnd/(?P<court_id>[0-9]+)/(?P<date>[0-9]+)/(?P<time>[0-9]+)/(?P<rpi_data>[a-zA-Z]+)/$', views.add_value, name = 'add_value'),
]
