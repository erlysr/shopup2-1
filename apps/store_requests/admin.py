from django.contrib import admin
from .models import RentType, StoreRequest


class RentTypeAdmin(admin.ModelAdmin):

    list_display = ['name_type']


class StoreRequestAdmin(admin.ModelAdmin):
    #Checar como cambiar las etiquetas a espanol para que acepte acentos
    list_display = (
        'Contacto',
        'Telefono',
        'Email',
        'Giro',
        'Renta',
        'Fecha_Inicio',
        'Fecha_Termino',
        'Precio',
        'status_type'
    )
    ordering = ('-status_type', )
    # list_filter = ('store_name', 'status')
    # search_fields = (
    #     'store_name',
    #     'contact__firstname',
    #     'address__address_line1',
    #     'address__neighborhood'
    # )
    list_editable = ('status_type', )
    # inlines = [Store_RequestInLine, ]
    # change_list_template = "admin/change_list_filter_sidebar.html"

    # Register your models here.

admin.site.register(RentType, RentTypeAdmin)
admin.site.register(StoreRequest, StoreRequestAdmin)
