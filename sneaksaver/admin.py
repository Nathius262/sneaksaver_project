from django.contrib import admin
from .models import Clean, CleanService, Review, Booking, Contact, Product, ShoeModel, Message

# Register your models here.
class CleanAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'status']
    

class CleanServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name']
    
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_created']
    

class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'date']
    

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'date']
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    
class ShoeModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    
    
admin.site.register(Clean, CleanAdmin)
admin.site.register(CleanService, CleanServiceAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ShoeModel, ShoeModelAdmin)
admin.site.register(Message)