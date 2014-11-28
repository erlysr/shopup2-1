from django.contrib import admin
from .models import Tabulator


class TabulatorAdmin(admin.ModelAdmin):
    list_display = (
        'town',
        'estado',
        'precio_minimo',
        'precio_maximo',
        'media_precio',
        'suggested_price'
    )
    list_editable = ('suggested_price', )
    ordering = ('town', )
    list_filter = ('town', 'town__city__state')
    search_fields = ('town', )

    change_list_template = "admin/change_list_filter_sidebar.html"

# Register your models here.
admin.site.register(Tabulator, TabulatorAdmin)
