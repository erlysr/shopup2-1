from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(
        r'^signup/',
        views.RegisterProfile.as_view(),
        name='signup'
    ),
    url(r'^signin/$', views.LoginView.as_view(), name='signin'),
    url(r'^logout/$', views.logout_view, name='logout'),
)
