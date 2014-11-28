from django.contrib import admin
from .models import Popular_Topup


class PopularTopupAdmin(admin.ModelAdmin):
    filter_horizontal = ('store_n', )

# Register your models here.
admin.site.register(Popular_Topup, PopularTopupAdmin)
