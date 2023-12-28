from django.db import models
from authentication.models import CustomUser
from .utils import upload_location

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="user_profile", null=True, blank=False)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)