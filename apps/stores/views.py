from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.core.urlresolvers import reverse

from . forms import (
    RegStoreStepOneForm, RegStoreStepTwoForm, RegStoreStepThreeForm)

from . models import Store, Contact

# Registro de tiendas


class RegStoreStepOneView(CreateView):
    """ Creacion del contacto """
    """ almacenar datos temporalmente en session """
    form_class = RegStoreStepOneForm
    template_name = 'reg_store_step_one.html'

    def get_success_url(self):
        return reverse('stores:reg-store-2', args=(self.object.pk,))


class RegStoreStepTwoView(CreateView):
    """ almacenar datos temporalmente en session """
    form_class = RegStoreStepTwoForm
    model = Store
    success_url = '/'
    template_name = 'reg_store_step_two.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        obj = Contact.objects.get(pk=pk)
        return obj

    def get_form_kwargs(self):
        kwargs = super(RegStoreStepTwoView, self).get_form_kwargs()
        kwargs.update({'contact': self.get_object()})
        return kwargs

    def get_success_url(self):
        return reverse('create-personal', args=(self.object.pk,))


class RegStoreStepThreeView(UpdateView):
    """ almacenar datos temporalmente en session """
    form_class = RegStoreStepThreeForm
    template_name = 'reg_store_step_two.html'
    success_url = '/stores/reg/step/three/'

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
