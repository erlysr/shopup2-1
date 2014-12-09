from django.views.generic import ListView
from stores.models import Store
from userprofiles.forms import EmailAuthenticationForm, ProfileForm

class Home(ListView):

    template_name = 'home.html'
    queryset = Store.objects.filter(status__name='Aprobada')
    paginate_by = 4
    

    def get_context_data(self, **kwargs):
    	form_login = EmailAuthenticationForm(request.POST or None)
    	form_profile = ProfileForm(request.POST or None)
        context = super(Home, self).get_context_data(**kwargs)
        context['form_login'] = form_login
        context['form_profile'] = form_profile
        
        return context
