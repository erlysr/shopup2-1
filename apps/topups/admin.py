from django.contrib import admin
from .models import Topup


class TopupsAdmin(admin.ModelAdmin):
    list_display = ('topup_name', 'Imagen')
    prepopulated_fields = {'slug': ('topup_name',)}

admin.site.register(Topup, TopupsAdmin)
