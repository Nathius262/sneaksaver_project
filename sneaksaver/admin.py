from django.contrib import admin
from .models import Clean, CleanService, Review, Booking

# Register your models here.
class CleanAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'status']
    

class CleanServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name']
    
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_created']
    

class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'date']
    
    
admin.site.register(Clean, CleanAdmin)
admin.site.register(CleanService, CleanServiceAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Booking, BookingAdmin)