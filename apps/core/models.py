# -*- coding: utf-8 -*-


from django.db import models

from localflavor.mx.models import MXZipCodeField

from core.utils import rm_double_space


class Country(models.Model):
    country_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.country_name


class State(models.Model):
    state_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.state_name


class City(models.Model):
    city_name = models.CharField(max_length=255)
    state = models.ForeignKey(State)

    def __unicode__(self):
        return self.city_name


class Town(models.Model):
    # Delegacion / Municipio
    town_name = models.CharField(max_length=255)
    city = models.ForeignKey(City)

    class Meta:
        ordering = ['town_name']

    def __unicode__(self):
        return '{} | {}'.format(self.town_name, self.city.__unicode__())


class PostalCode(models.Model):
    postal_code_key = MXZipCodeField()
    town = models.ForeignKey(Town)

    def __unicode__(self):
        return self.postal_code_key


class Neighborhood(models.Model):
    # colonia
    name = models.CharField(max_length=64)
    postal_code = models.ForeignKey(PostalCode)


class Address(models.Model):

    # calle...tal
    street = models.CharField(max_length=255)

    # ext
    outside_number = models.PositiveSmallIntegerField(blank=True, null=True)

    # int
    interior_number = models.PositiveSmallIntegerField(blank=True, null=True)

    # colonia
    neighborhood = models.CharField(max_length=255)

    def __unicode__(self):
        cad = rm_double_space(self.street)
        if self.outside_number:
            cad += ' Ext %i' % self.outside_number
        if self.interior_number:
            cad += ' Int %i' % self.interior_number
        cad += ' %s' % rm_double_space(self.neighborhood)
        cad += ', %s' % self.neighborhood.postal_code
        return cad
