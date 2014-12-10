# -*- coding: utf-8 -*-

from django.views.generic import ListView

from . models import Topup


class TopupList(ListView):

    template_name = 'topups.html'
    model = Topup
