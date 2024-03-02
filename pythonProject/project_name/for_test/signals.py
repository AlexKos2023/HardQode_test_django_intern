from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from .utils import access_product

@receiver(post_save, sender=Product)
def handle_product_access(sender, instance, created, **kwargs):
    if created:
        access_product(instance.product, instance.user)
