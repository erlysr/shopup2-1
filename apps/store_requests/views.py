from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView

from . forms import StoreRequestForm


class StoreRequestView(FormView):

    form_class = StoreRequestForm
    template_name = 'store_request.html'
    success_url = '/request/stores/success'

    def get_form_kwargs(self):
        kwargs = super(StoreRequestView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())


class SuccessStoreRequest(TemplateView):

    template_name = 'success_store_request.html'
