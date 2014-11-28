from django.contrib import admin


from . models import (
    Country, State, City, Town, PostalCode, Neighborhood)


class CountryAdmin(admin.ModelAdmin):

    list_display = ['country_name']


class StateAdmin(admin.ModelAdmin):

    list_display = ['state_name', 'country']


class CityAdmin(admin.ModelAdmin):

    list_display = ['city_name', 'state']


class TownAdmin(admin.ModelAdmin):

    list_display = ['town_name', 'city']


class PostalCodeAdmin(admin.ModelAdmin):

    list_display = ['postal_code_key', 'town']


class NeighborhoodAdmin(admin.ModelAdmin):

    list_display = ['name', 'postal_code']


admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Town, TownAdmin)
admin.site.register(PostalCode, PostalCodeAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
