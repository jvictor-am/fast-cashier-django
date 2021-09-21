# third party imports
from rest_framework.viewsets import  ModelViewSet
from rest_framework import status
from rest_framework import exceptions
from rest_framework.decorators import action
from rest_framework.response import Response

# local imports
from .models import Customer
from .models import Order
from .models import Product
from .models import Seller
from .serializers import OrderCreateSerializer
from .serializers import OrderItemSerializer
from .serializers import ProductSerializer
from .serializers import CustomerSerializer
from .serializers import SellerSerializer
from .serializers import OrderSerializer
from .utils import order_total_commission
from .utils import period_dates
from .filters import OrderFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        variable_commission_percentage = self.request.data.get('variable_commission_percentage', None)
        if variable_commission_percentage:
            return Response(
                data={'error': 'Não deve conter valor para campo de comissão variável'},
                status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


    @action(detail=True)
    def commission(self, request, *args, **kwargs):
        """Total commission's seller by date range"""

        seller = self.get_object()

        try:
            start_date, end_date = period_dates(self.request.query_params)
            orders = Order.objects.filter(seller__pk=seller.pk, created__range=[start_date, end_date])
            period_total_commission = sum(order_total_commission(order) for order in orders.all())
        except Exception as e:
            return Response({'error': e.__str__()})

        return Response({'period_total_commission': period_total_commission, 'quantity_of_orders': orders.count()})


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    filter_class = OrderFilter

    def get_serializer_class(self):
        method = self.request.method
        serializer_class = OrderSerializer

        if method == 'POST':
            serializer_class = OrderCreateSerializer

        return serializer_class

    def perform_create(self, serializer):
        items = self.request.data.get('items')

        if not items:
            raise exceptions.ValidationError({
                'items': 'Please provide items for this order'
            })

        order_items_serialized = OrderItemSerializer(data=items, many=True)
        order_items_serialized.is_valid(raise_exception=True)

        order = serializer.save()
        order_items_serialized.save(order=order)
