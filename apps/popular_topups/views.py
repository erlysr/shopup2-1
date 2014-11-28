from django.views.generic import ListView
from popular_topups.models import Popular_Topup


class TopupListView(ListView):
    model = Popular_Topup
    template_name = 'popular_topup.html'

    def get_queryset(self):
        if self.kwargs.get('topup'):
            queryset = self.model.objects.filter(
                topup__topup_name__contains=self.kwargs['topup']
            )
        else:
            queryset = super(TopupListView, self).get_queryset()
        return queryset
