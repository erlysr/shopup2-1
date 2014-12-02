# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(
        r'stores/$',
        views.StoreRequestView.as_view(),
        name='store-request'
    ),
)
