from django.conf.urls import patterns, url

from . import ajax

urlpatterns = patterns(
    '',
    url(
        r'^ajax/postal-codes/$',
        ajax.PostalCodesAjax.as_view(),
        name='ajax-postal-codes'
    )
)
