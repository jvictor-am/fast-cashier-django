# Third party imports
import django_filters

# Local imports
from .models import Order
from .models import Seller


class OrderFilter(django_filters.FilterSet):
    seller = django_filters.ModelChoiceFilter(field_name='seller__name', queryset=Seller.objects.all())

    class Meta:
        model = Order
        fields = ['seller']
