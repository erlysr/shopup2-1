from django.db import models


class Status_Type(models.Model):
    status_name = models.CharField(max_length=11)

    def __unicode__(self):
        return self.status_name
