# django imports
from django.contrib import admin

# local imports
from .models import Product
from .models import Customer
from .models import Seller
from .models import Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'fixed_commission_percentage')
    readonly_fields=('variable_commission_percentage', )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'customer')