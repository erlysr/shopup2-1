from django.views.generic import ListView

from stores.models import Store


class Home(ListView):

    template_name = 'home.html'
    queryset = Store.objects.filter(status__name='Aprobada')
    paginate_by = 4
