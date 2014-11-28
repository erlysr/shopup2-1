from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class News(models.Model):
	news_text = models.TextField()
	username = models.ForeignKey(User)
	time_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.username.first_name

	def Usuario(self):
		return self.username.firstname

	def Noticia(self):
		return self.news_text