from django.core import serializers
from django.http import JsonResponse
from django.views.generic import TemplateView

from . models import PostalCode


class PostalCodesAjax(TemplateView):

    def get(self, request, *args, **kwargs):
        print request.GET['id']
        codes = PostalCode.objects.filter(town__id=request.GET['id'])
        data = serializers.serialize(
            'json',
            codes,
            fields=('postal_code_key',)
        )
        return JsonResponse(data, safe=False)
