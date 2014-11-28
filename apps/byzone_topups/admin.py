from django.contrib import admin
from .models import Byzone_Topup

class Byzone_TopupAdmin(admin.ModelAdmin):
	filter_horizontal = ('store', )
# Register your models here.
admin.site.register(Byzone_Topup, Byzone_TopupAdmin)