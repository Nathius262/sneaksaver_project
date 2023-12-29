from django.db import models
from authentication.models import CustomUser
from .utils import upload_location

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="user_profile", null=True, blank=False)
    first_name=models.CharField(max_length=50, null=True, blank=True)
    last_name=models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    
    
class Reward(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=False)
    point = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.CharField(max_length=50, null=True, blank=False)
    
    def __str__(self):
        return str(self.user)
    