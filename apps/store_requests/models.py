# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

from stores.models import Store, StatusType


class RentType(models.Model):
    name_type = models.CharField(max_length=255)

    # menos de 7 dias --> renta por dia
    # en medio:: --> renta semanal
    # mas de 30 dias --> renta mensual
    def __unicode__(self):
        return self.name_type


class StoreRequest(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store)
    user = models.ForeignKey(User)
    rent_type = models.ForeignKey(RentType)
    rent_price = models.FloatField(null=True, blank=True, default=0)
    status_type = models.ForeignKey(StatusType)  # default 'nueva'
    # Dos input --> jquery ui --> widget calendario
    start_date = models.DateField()
    ending_date = models.DateField()

    class Meta:
        verbose_name = 'Petición de Tienda'
        verbose_name_plural = 'Peticiones de Tiendas'

    def __unicode__(self):
        return self.store.__unicode__(), self.user.__unicode__()

    # def Contacto(this):
    #     return this.contact.firstname

    # def Giro(this):
    #     return this.store.activity

    # def Renta(this):
    #     return this.rent_type.name_type

    # def Precio(this):
    #     return this.rent_price

    # def Status(this):
    #     return this.status_req.status_name

    # def Fecha_Inicio(this):
    #     return this.start_date

    # def Fecha_Termino(this):
    #     return this.ending_date
