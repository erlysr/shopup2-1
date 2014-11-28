from django.contrib import admin
from .models import Store_Request


class Store_RequestAdmin(admin.ModelAdmin):
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
        'status_req'
    )
    ordering = ('-status_req', )
    # list_filter = ('store_name', 'status')
    # search_fields = (
    #     'store_name',
    #     'contact__firstname',
    #     'address__address_line1',
    #     'address__neighborhood'
    # )
    list_editable = ('status_req', )
    # inlines = [Store_RequestInLine, ]
    # change_list_template = "admin/change_list_filter_sidebar.html"

    # Register your models here.

admin.site.register(Store_Request, Store_RequestAdmin)
