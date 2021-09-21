# python imports
import datetime

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
        commission = ''
        if item.product.variable_commission_percentage:
            commission = item.product.variable_commission_percentage
        else:
            commission = item.product.fixed_commission_percentage

        response.append((commission/100)*item.product.price*item.quantity)

    return sum(response)
