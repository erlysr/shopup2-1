from django.contrib.auth.models import User
from django.db import models

from stores.models import Store


class RentType(models.Model):
    name_type = models.CharField(max_length=255)

    # menos de 7 dias --> renta por dia
    # en medio:: --> renta semanal
    # mas de 30 dias --> renta mensual
    def __unicode__(self):
        return self.name_type


class StatusType(models.Model):
    status_name = models.CharField(max_length=11)

    def __unicode__(self):
        return self.status_name


class StoreRequest(models.Model):

    request_code = models.CharField(max_length=6)
    store = models.ForeignKey(Store)
    user = models.ForeignKey(User)
    # contact = models.ForeignKey(Contact)
    date_created = models.DateTimeField(auto_now_add=True)
    rent_type = models.ForeignKey(RentType)
    rent_price = models.FloatField(null=True, blank=True, default=0)
    status_req = models.ForeignKey(StatusType)  # default 'nueva'
    # Dos input --> jquery ui --> widget calendario
    start_date = models.DateField()
    ending_date = models.DateField()

    def __unicode__(self):
        return self.request_code

    def Contacto(this):
        return this.contact.firstname

    def Telefono(this):
        return this.contact.contact_phone

    def Email(this):
        return this.contact.email

    def Giro(this):
        return this.store.activity

    def Renta(this):
        return this.rent_type.name_type

    def Precio(this):
        return this.rent_price

    def Status(this):
        return this.status_req.status_name

    def Fecha_Inicio(this):
        return this.start_date

    def Fecha_Termino(this):
        return this.ending_date
