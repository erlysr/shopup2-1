# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(
        r'^reg/step/one/$',
        views.RegStoreStepOneView.as_view(),
        name='reg-store-1'
    ),
    url(
        r'^reg/step/two/$',
        views.RegStoreStepTwoView.as_view(),
        name='reg-store-2'
    ),
    url(
        r'^reg/step/three/$',
        views.RegStoreStepThreeView.as_view(),
        name='reg-store-3'
    ),
    url(
        r'^reg/step/four/$',
        views.RegStoreStepFourView.as_view(),
        name='reg-store-4'
    ),
)
