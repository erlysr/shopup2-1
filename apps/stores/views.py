# from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView, DetailView

from . forms import (
    RegStoreStepOneForm, RegStoreStepTwoForm, RegStoreStepThreeForm,
    RegStoreStepFourForm)

from . models import Store

# Registro de tiendas


class RegStoreStepOneView(FormView):
    """ Creacion del contacto """
    form_class = RegStoreStepOneForm
    template_name = 'reg_store_step_one.html'

    def get_success_url(self):
        return reverse('stores:reg-store-2')

    def form_valid(self, form):
        self.request.session['fmr_one'] = self.request.POST.copy()
        # for k, v in form.cleaned_data.iteritems():
        #     self.request.session[k] = v
        return HttpResponseRedirect(self.get_success_url())


class RegStoreStepTwoView(FormView):
    form_class = RegStoreStepTwoForm
    template_name = 'reg_store_step_two.html'

    def get_success_url(self):
        return reverse('stores:reg-store-3')

    def form_valid(self, form):
        self.request.session['fmr_two'] = self.request.POST.copy()
        return HttpResponseRedirect(self.get_success_url())


class RegStoreStepThreeView(FormView):
    form_class = RegStoreStepThreeForm
    template_name = 'reg_store_step_two.html'

    def get_success_url(self):
        return reverse('stores:reg-store-4')

    def form_valid(self, form):
        self.request.session['fmr_three'] = self.request.POST.copy()
        return HttpResponseRedirect(self.get_success_url())


class RegStoreStepFourView(FormView):
    form_class = RegStoreStepFourForm
    template_name = 'reg_store_step_two.html'
    success_url = '/'

    def form_valid(self, form):
        user = User.objects.get(username='jrperdomoz')
        contact = RegStoreStepOneForm(self.request.session['fmr_one']).save()
        fmr_two = self.request.session['fmr_two']
        fmr_two[u'contact'] = contact
        fmr_two[u'user'] = user
        fmr_three = self.request.session['fmr_three']
        data = dict(
            fmr_two.items() + fmr_three.items() + self.request.POST.items()
        )
        store = Store()
        store.user = data['user']
        store.contact = data['contact']
        store.store_name = data['store_name']
        store.dimentions = data['dimentions']
        store.activity = data['activity']
        store.store_phone = data['store_phone']
        store.website = data['website']
        store.facebook = data['facebook']
        store.twitter = data['twitter']
        store.youtube = data['youtube']

        if 'wireless' in data:
            store.wireless = True
        if 'stands' in data:
            store.stands = True
        if 'repisas' in data:
            store.repisas = True
        if 'boards' in data:
            store.boards = True
        if 'lighting' in data:
            store.lighting = True
        if 'electricity' in data:
            store.electricity = True
        if 'water' in data:
            store.water = True
        if 'airconditioning' in data:
            store.airconditioning = True
        if 'toilets' in data:
            store.toilets = True
        if 'heating' in data:
            store.heating = True
        if 'elevator' in data:
            store.elevator = True
        if 'parkinglot' in data:
            store.parkinglot = True
        if 'mostrador' in data:
            store.mostrador = True
        if 'phoneline' in data:
            store.phoneline = True
        if 'storehouse' in data:
            store.storehouse = True
        if 'dressingroom' in data:
            store.dressingroom = True
        store.save()
        return HttpResponseRedirect(self.get_success_url())

# Listado de tiendas


class StoreListView(ListView):
    model = Store
    template_name = 'stores_topups.html'
    paginate_by = 4

    def get_queryset(self):
        if self.kwargs.get('tabulator'):
            # Hay que cambiar el nombre del campo a 'tabulator' en tabulators
            queryset = self.model.objects.filter(
                tabulator__tab_zone__contains=self.kwargs['tabulator']
            )
        else:
            queryset = super(StoreListView, self).get_queryset()
        return queryset


class StoreDetailView(DetailView):
    model = Store
    template_name = "store_detail.html"
    slug_url_kwarg = "store_name"
    slug_field = "store_name"
