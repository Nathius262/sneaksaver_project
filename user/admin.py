from django.contrib import admin
from .models import Profile, Reward

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user',]


class RewardAdmin(admin.ModelAdmin):
    list_display = ['user', 'point']
    
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Reward, RewardAdmin)