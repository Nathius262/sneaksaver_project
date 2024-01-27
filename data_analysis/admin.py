from django.contrib import admin
from .models import ProductSearch, CleanServiceSearch, TopSearch, FrequentlyAskedQuestion

# Register your models here.
admin.site.register(ProductSearch)
admin.site.register(TopSearch)
admin.site.register(CleanServiceSearch)
admin.site.register(FrequentlyAskedQuestion)