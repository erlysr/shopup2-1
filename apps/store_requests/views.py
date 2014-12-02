from django.views.generic import FormView

from . forms import StoreRequestForm


class StoreRequestView(FormView):

    form_class = StoreRequestForm
    template_name = 'store_request.html'
