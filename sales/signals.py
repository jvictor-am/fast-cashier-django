# python imports
from datetime import datetime

# django imports
from django.db.models.signals import post_save
from django.dispatch import receiver

# local imports
from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def order_post_save(sender, instance, **kwargs):
    product = instance.product

    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    noon = now.replace(hour=12, minute=0, second=0, microsecond=0)

    if (midnight<=now<=noon) and product.fixed_commission_percentage > 5:
        product.variable_commission_percentage = 5
        product.save(update_fields=['variable_commission_percentage'])
    if (noon<now<midnight) and product.fixed_commission_percentage < 4:
        product.variable_commission_percentage = 4
        product.save(update_fields=['variable_commission_percentage'])
