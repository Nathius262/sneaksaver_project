from django.db import models
from user.models import Profile
from .utils import upload_location
from django.urls import reverse

# Create your models here.
class CleanService(models.Model):
    service_name = models.CharField(max_length=50, null=True, blank=False)
    service_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=False)
    
    def __str__(self):
        return self.service_name
    
    
class Clean(models.Model):
    user= models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=False, related_name="user_clean")
    service = models.ForeignKey(CleanService, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user)
    

class Review(models.Model):
    user= models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=False, related_name="user_review")
    clean_service = models.ForeignKey(Clean, on_delete=models.CASCADE, related_name="clean_service_review")
    message = models.TextField()
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return str(self.user)
    
    
class Booking(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="user_booking", null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=False)
    email = models.CharField(max_length=100, null=True, blank=False)
    package = models.ForeignKey(CleanService, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=False)
    
    
    def __str__(self):
        return str(self.name)
    
        
class Contact(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="user_contact", null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=False)
    email = models.CharField(max_length=100, null=True, blank=False)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.name)
    
    
class Product(models.Model):
    name=models.CharField(max_length=50, null=True, blank=True)
    description=models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=False)
    image = models.ImageField(upload_to=upload_location, default="default_product.jpg", null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return str(self.name)
    
    @property
    def image_url(self):
        try:
            pic = self.image.url
        except :
            pic = ''
        return pic
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])
    