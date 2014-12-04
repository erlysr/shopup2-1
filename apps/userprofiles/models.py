from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    usuario = models.OneToOneField(User)
    user_phone = models.CharField(max_length=12)
    avatar = models.ImageField(upload_to='userprofiles', blank=True)
    calification = models.SmallIntegerField(default=3)

    def __unicode__(self):
        return self.username.username

    def foto_avatar(self):
        return """
            <img src="%s" height="100" widht="42"></img>
            """ % (self.avatar.url)

    foto_avatar.allow_tags = True
