from django.db import models
from sneaksaver.models import Product, CleanService

# Create your models here.
class ProductSearch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=True)
    search_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.product} - Searches: {self.search_count}'
    

class CleanServiceSearch(models.Model):
    service = models.ForeignKey(CleanService, on_delete=models.CASCADE, blank=False, null=True)
    search_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.service} - Searches: {self.search_count}'
    

