from django.db import models
from user.models import Profile

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
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="user_booking")
    date = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return str(self.user)