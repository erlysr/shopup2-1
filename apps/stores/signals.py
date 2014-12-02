# -*- coding: utf-8 -*-

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from . models import Store


@receiver(pre_delete, sender=Store)
def delete_images(sender, instance, using, **kwargs):

    instance.logo.delete(save=False)
    if instance.image2:
        instance.image2.delete(save=False)
    if instance.image3:
        instance.image3.delete(save=False)
    if instance.image4:
        instance.image4.delete(save=False)
    if instance.image5:
        instance.image5.delete(save=False)
