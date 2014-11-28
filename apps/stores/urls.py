# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url

from . views import RegStoreStepOneView, RegStoreStepTwoView


urlpatterns = patterns(
    '',
    url(
        r'^reg/step/one/$',
        RegStoreStepOneView.as_view(),
        name='reg-store-1'
    ),
    url(
        r'^reg/step/two/(?P<pk>\d+)/$',
        RegStoreStepTwoView.as_view(),
        name='reg-store-2'
    ),
)
