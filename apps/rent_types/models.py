from django.db import models


class Rent_Type(models.Model):
    name_type = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name_type
