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
    

class TopSearch(models.Model):
    name = models.CharField(max_length=500, null=True)
    search_count = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.name} - Searches: {self.search_count}'
    
    
class FrequentlyAskedQuestion(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    date = models.DateField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.title