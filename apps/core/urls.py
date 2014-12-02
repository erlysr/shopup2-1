from django.conf.urls import patterns, url

from . import views
from . import ajax

urlpatterns = patterns(
    '',
    url(r'^$', views.Home.as_view(), name='home'),
    #
    # urls for ajax
    url(
        r'^ajax/postal-codes/$',
        ajax.PostalCodesAjax.as_view(),
        name='ajax-postal-codes'
    ),
)
