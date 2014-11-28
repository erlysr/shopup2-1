from django.contrib.auth.models import User
from django.db import models

from rent_types.models import Rent_Type

from status_types.models import Status_Type

from stores.models import Store, Contact


class Store_Request(models.Model):
    request_code = models.CharField(max_length=6)
    store = models.ForeignKey(Store)
    username = models.ForeignKey(User)
    contact = models.ForeignKey(Contact)
    date_created = models.DateTimeField(auto_now_add=True)
    rent_type = models.ForeignKey(Rent_Type)
    rent_price = models.FloatField(null=True, blank=True, default=0)
    status_req = models.ForeignKey(Status_Type)
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
