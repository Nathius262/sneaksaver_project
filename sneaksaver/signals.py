from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Product
import uuid


@receiver(pre_save, sender=Product)
def createUserProfile(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = str(uuid.uuid4()).replace("-", "")[:12]