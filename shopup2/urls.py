
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from stores.views import StoreListView, StoreDetailView

from popular_topups.views import TopupListView

from userprofiles.views import (
    ProfileView, PerfilRedirectView
)


urlpatterns = patterns(
    '',
    # includes urls
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^', include('userprofiles.urls', namespace='userprofiles')),
    url(r'^stores/', include('stores.urls', namespace='stores')),
    url(r'^request/', include('store_requests.urls', namespace='storerequest')),
    url(r'^topups/', include('topups.urls', namespace='topups')),

    # urls directas
    # url(
    #     r'^stores/(?P<StoreName>[\w\-]+)/',
    #     'stores.views.StoreView',
    #     name='StoreView'
    # ),


    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(
        r'^perfil/$', PerfilRedirectView.as_view(url='/signup/'), name='perfil'
    ),
    url(r'^topups/$', TopupListView.as_view(), name='topup_list'),
    url(
        r'^topups/(?P<topup>[\w\-]+)/$',
        TopupListView.as_view(),
        name='topup_list'
    ),
    url(
        r'^stores/topups/$',
        StoreListView.as_view(),
        name='stores_topups_list'
    ),
    url(
        r'^stores/topups/(?P<tabulator>[\w\-]+)/$',
        StoreListView.as_view(),
        name='stores_topups_list'
    ),
    url(
        r'^store/detail/(?P<store_name>[\w\-]+)/$',
        StoreDetailView.as_view(),
        name='store_detail'
    ),
    # url(
    #     r'^media/(?P<path>.*)$',
    #     'django.views.static.serve',
    #     {'document_root': settings.MEDIA_ROOT}),
    # url(
    #     r'^static/(?P<path>.*)$',
    #     'django.views.static.serve',
    #     {'document_root': settings.STATIC_ROOT}),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
