# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from core.models import Address
from tabulators.models import Tabulator


class Contact(models.Model):

    firstname = models.CharField('Nombre', max_length=255)
    lastname = models.CharField('Apellidos', max_length=255)
    email = models.CharField(max_length=255)
    contact_phone = models.CharField('Teléfono', max_length=12)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __unicode__(self):
        return self.firstname


class StatusType(models.Model):
    status_name = models.CharField(max_length=11)

    def __unicode__(self):
        return self.status_name


class Store(models.Model):

    user = models.ForeignKey(User, blank=True, null=True)

    # 1ra Forma:: Registro de tienda
    contact = models.ForeignKey(Contact, blank=True, null=True)

    # 2da Forma:: Registro de tienda
    store_name = models.CharField(max_length=255)
    dimentions = models.FloatField()  # Mts2
    activity = models.CharField(max_length=255)  # Giro
    store_phone = models.CharField(max_length=12)

    # Funciones Ajax:: A partir de un estado, desplegar
    # Delegaciones o Municipios, Luego apartir de la delegacion
    # cargar los codigos postales correspondientes.
    address = models.ForeignKey(Address, blank=True, null=True)

    # 3ra Forma
    website = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    youtube = models.CharField(max_length=255, blank=True)

    # Las imagenes des pues del registro
    image1 = models.ImageField(upload_to='stores')  # logotipo ?
    image2 = models.ImageField(upload_to='stores', blank=True)
    image3 = models.ImageField(upload_to='stores', blank=True)
    image4 = models.ImageField(upload_to='stores', blank=True)
    image5 = models.ImageField(upload_to='stores', blank=True)

    # 4ta Forma
    wireless = models.BooleanField(default=False)
    stands = models.BooleanField(default=False)
    repisas = models.BooleanField(default=False)
    boards = models.BooleanField(default=False)
    lighting = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    water = models.BooleanField(default=False)

    airconditioning = models.BooleanField(default=False)
    toilets = models.BooleanField(default=False)
    heating = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    parkinglot = models.BooleanField(default=False)
    mostrador = models.BooleanField(default=False)
    phoneline = models.BooleanField(default=False)
    storehouse = models.BooleanField(default=False)
    dressingroom = models.BooleanField(default=False)

    comments = models.TextField(blank=True)
    tabulator = models.ForeignKey(Tabulator, blank=True, null=True)
    status = models.ForeignKey(StatusType, blank=True, null=True)
    date_created = models.DateField(null=True, blank=True)
    date_approved = models.DateField(null=True, blank=True)
    counter = models.BooleanField(default=False)

    #Ojo: Faltan los campos para los lugares cercanos

    price = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = 'Tienda'
        verbose_name_plural = 'Tiendas'

    def __unicode__(self):
        return self.store_name

    # def precio_por_dia(self):
    #     return self.tabulator.suggested_price

    def precio_por_semana(self):
        precio_semana = (self.tabulator.suggested_price * 6) * .95
        return precio_semana

    def precio_por_mes(self):
        precio_mes = (self.tabulator.suggested_price * 30) * .90
        return precio_mes

    def tienda(self):
        return self.store_name

    def contacto(self):
        return self.contact

    def telefono(self):
        return self.store_phone

    def correo(self):
        return self.contact.email

    def direccion(self):
        return u'direccion'
        # return """
        #     <p>%s,</p>
        #     <p>%s,</p>
        #     <p>%s,</p>
        #     <p>%s,</p>
        #     <p>%s,</p>
        #     """ % (
        #     self.address,
        #     self.address.neighborhood,
        #     self.address.postal_code,
        #     self.address.postal_code.town,
        #     self.address.postal_code.town.city
        # )

    def verificacion(self):
        return self.status

    #Falta hacer la funcion para calcular el num. de solicitudes
    def solicitudes(self):
        return '5'

    def editastatus(self):
        return self.status.status_name

    direccion.allow_tags = True
    direccion.admin_order_field = 'address'
    tienda.admin_order_field = 'store_name'
    contacto.admin_order_field = 'contact'
    verificacion.admin_order_field = 'status'

    #Falta ordenar por solicitudes
