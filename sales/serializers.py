# third party imports
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from rest_framework import serializers

# local imports
from .models import Order
from .models import OrderItem
from .models import Product
from .models import Customer
from .models import Seller
from .utils import order_total_commission


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'fixed_commission_percentage', 'variable_commission_percentage']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name']


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'name']


class OrderItemSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(source='product.price', max_digits=9, decimal_places=2, read_only=True)
    fixed_commission_percentage = serializers.DecimalField(
        source='product.fixed_commission_percentage',
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        read_only=True)
    variable_commission_percentage = serializers.DecimalField(
        source='product.variable_commission_percentage',
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'price', 'quantity', 'fixed_commission_percentage', 'variable_commission_percentage']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    total_commission= serializers.SerializerMethodField()
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    seller_name = serializers.CharField(source='seller.name', read_only=True)


    class Meta:
        model = Order
        fields = ['id', 'created', 'customer_name', 'seller_name', 'total_price', 'total_commission', 'items']


    def get_total_price(self, obj):
        response = []
        for item in OrderItem.objects.filter(order=obj):
            response.append(item.product.price*item.quantity)

        return sum(response)

    def get_total_commission(self, obj):
        return order_total_commission(obj)


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'seller']
