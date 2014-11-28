from django.contrib import admin

from store_requests.models import Store_Request

from . models import Store, Contact


class ContactAdmin(admin.ModelAdmin):

    list_display = ['firstname', 'lastname', 'email', 'contact_phone']


class Store_RequestInLine(admin.StackedInline):
    model = Store_Request
    extra = 0


class StoreAdmin(admin.ModelAdmin):
    #Checar como cambiar las etiquetas a espanol para que acepte acentos
    list_display = (
        'tienda',
        'contact',  # idioma
        'telefono',
        'correo',
        'direccion',
        'status',
        'solicitudes',
        'precio_por_dia',
        'precio_por_semana',
        'precio_por_mes'
    )
    ordering = ('-status', 'store_name')
    list_filter = ('store_name', 'status')
    search_fields = (
        'store_name',
        'contact__firstname',
        'address__address_line1',
        'address__neighborhood'
    )
    list_editable = ('status', )
    inlines = [Store_RequestInLine, ]
    change_list_template = "admin/change_list_filter_sidebar.html"

admin.site.register(Store, StoreAdmin)
admin.site.register(Contact, ContactAdmin)
