# django imports
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

# third party imports
from django_extensions.db.models import TimeStampedModel


class Product(TimeStampedModel):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    fixed_commission_percentage = models.DecimalField(
        max_digits=4, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(10)])
    variable_commission_percentage = models.DecimalField(
        max_digits=4, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(10)], null=True, blank=True)

    def __str__(self):
        return self.name


class Customer(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Seller(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Order(TimeStampedModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return ('Order %(id)s') % {'id': self.id}


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return str(self.product)
