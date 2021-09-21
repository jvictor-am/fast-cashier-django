# python imports
import datetime
import decimal

# django imports
from django.utils import timezone

# local imports
from.models import OrderItem


def period_dates(query_params):
    start_date_str = query_params.get('start_date', None)
    end_date_str = query_params.get('end_date', None)

    if not start_date_str or not end_date_str:
        raise Exception(
            "start_date and end_date must be used as query params in this format(yyyy-mm-dd).")

    end_time_with_complete_day = datetime.datetime.strptime(end_date_str, "%Y-%M-%d") + datetime.timedelta(days=1)
    end_date_str = datetime.datetime.strftime(end_time_with_complete_day, "%Y-%M-%d")

    return start_date_str, end_date_str

def order_total_commission(obj):
    response = []

    for item in OrderItem.objects.filter(order=obj):

        created_data_from_model = item.order.created # it comes with UTC timezone (-3 hours)
        created_data_adjusted_to_local_time = timezone.localtime(created_data_from_model)

        midnight_same_day = created_data_adjusted_to_local_time.replace(hour=0, minute=0, second=0, microsecond=0)
        before_midnight_next_day = created_data_adjusted_to_local_time.replace(hour=23, minute=59, second=59, microsecond=59)
        noon = created_data_adjusted_to_local_time.replace(hour=12, minute=0, second=0, microsecond=0)

        commission = item.product.fixed_commission_percentage

        if (midnight_same_day<=created_data_adjusted_to_local_time<=noon) and item.product.fixed_commission_percentage > 5:
            item.product.variable_commission_percentage = 5
            item.product.save(update_fields=['variable_commission_percentage'])
            commission = item.product.variable_commission_percentage
        if (noon<created_data_adjusted_to_local_time<before_midnight_next_day) and item.product.fixed_commission_percentage < 4:
            item.product.variable_commission_percentage = 4
            item.product.save(update_fields=['variable_commission_percentage'])
            commission = item.product.variable_commission_percentage

        response.append(decimal.Decimal(commission/100)*item.product.price*item.quantity)

    return sum(response)
