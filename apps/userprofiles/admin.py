from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'user_phone',
        'foto_avatar',
        'calification'
    )

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
