
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from stores.views import StoreListView, StoreDetailView

from popular_topups.views import TopupListView

from userprofiles.views import (
    ProfileView, LoginView, PerfilRedirectView, RegisterProfile)


urlpatterns = patterns(
    '',
    # includes urls
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stores/', include('stores.urls', namespace='stores')),
    url(r'^core/', include('core.urls', namespace='core')),

    # urls directas
    # url(
    #     r'^stores/(?P<StoreName>[\w\-]+)/',
    #     'stores.views.StoreView',
    #     name='StoreView'
    # ),
    url(
        r'^signup/',
        RegisterProfile.as_view(),
        name='signup'
    ),
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),
    url(r'^logout/', 'userprofiles.views.logout_view', name='logout'),
    url(r'^login/', LoginView.as_view(), name='login'),
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
        r'^stores_topups/$',
        StoreListView.as_view(),
        name='stores_topups_list'
    ),
    url(
        r'^stores_topups/(?P<tabulator>[\w\-]+)/$',
        StoreListView.as_view(),
        name='stores_topups_list'
    ),
    url(
        r'^store_detail/(?P<store_name>[\w\-]+)/$',
        StoreDetailView.as_view(),
        name='store_detail'
    )
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
