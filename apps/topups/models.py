from django.db import models


class Topup(models.Model):
    topup_name = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to='topups')
    image2 = models.ImageField(upload_to='topups', blank=True)
    image3 = models.ImageField(upload_to='topups', blank=True)

    def __unicode__(self):
        return self.topup_name

    def Imagen(self):
        return """
                <img src="%s" height="100" widht="42"></img>
                """ % (self.image1.url)

    Imagen.allow_tags = True
