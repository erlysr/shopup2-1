from django.db import models
from stores.models import Store
from topups.models import Topup


class Popular_Topup(models.Model):
    topup = models.ForeignKey(Topup)
    store_n = models.ManyToManyField('stores.Store')
    priority = models.IntegerField()

    def __unicode__(self):
        return self.topup.topup_name
