from django.db import models
from core.models import Town


class Tabulator(models.Model):
    tab_zone = models.CharField(max_length=255)
    town = models.ForeignKey(Town)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    media_price = models.IntegerField()
    suggested_price = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.tab_zone

    def delegacion(self):
        return self.town.town_name

    def precio_minimo(self):
        return self.min_price

    def precio_maximo(self):
        return self.max_price

    def media_precio(self):
        return self.media_price

    def estado(self):
        return self.town.city.state
