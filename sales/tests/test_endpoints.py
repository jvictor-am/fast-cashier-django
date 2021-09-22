# django imports
from django.urls import reverse

# third party imports
from model_bakery import baker
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_201_CREATED
from rest_framework.test import APITestCase
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ValidationError

# local imports
from ..models import Product
from ..models import Customer
from ..models import Seller
from ..models import Order


class TestProductViewSet(APITestCase):

    def setUp(self):
        self.url = reverse('product-list')

    def test_create_product(self):
        product = {
            'name': 'Teclado',
            'price': 300,
            'fixed_commission_percentage': 5
        }
        response = self.client.post(self.url, data=product)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_not_create_product_with_commission_above_limite(self):
        product = {
            'name': 'Teclado',
            'price': 300,
            'fixed_commission_percentage': 11
        }
        response = self.client.post(self.url, data=product)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_not_create_product_with_variable_commission_field(self):
        product = {
            'name': 'Teclado',
            'price': 300,
            'fixed_commission_percentage': 11,
            'variable_commission_percentage': 10
        }
        response = self.client.post(self.url, data=product)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_list_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTP_200_OK)


class TestCustomerViewSet(APITestCase):

    def setUp(self):
        self.url = reverse('customer-list')

    def test_create_customer(self):
        customer = {
            'name': 'Rodrigo'
        }
        response = self.client.post(self.url, data=customer)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)

    def test_list_customers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTP_200_OK)


class TestSellerViewSet(APITestCase):

    def setUp(self):
        self.url = reverse('seller-list')

    def test_create_seller(self):
        seller = {
            'name': 'Mairla'
        }
        response = self.client.post(self.url, data=seller)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Seller.objects.count(), 1)

    def test_list_sellers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTP_200_OK)


class TestOrderViewSet(APITestCase):
    def setUp(self):
        self.url = reverse('order-list')
        self.quantity = 5

        for index in range(5):
            baker.make(Product),
            baker.make(Customer),
            baker.make(Seller)

    def test_create_order(self):
        order = {
            "customer": 3,
            "seller": 4,
            "items": [
                {
                    "product": 3,
                    "quantity": 4
                }
            ]
        }
        response = self.client.post(self.url, data=order, format='json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

    def test_list_orders(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTP_200_OK)
