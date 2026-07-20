import pandas as pd

def clean_orders(orders):
    orders = orders.copy()
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    orders['expected_delivery_date'] = pd.to_datetime(orders['expected_delivery_date'])
    orders['actual_delivery_date'] = pd.to_datetime(orders['actual_delivery_date'])
    orders['delivery_delay_days'] = (orders['actual_delivery_date'] - orders['expected_delivery_date']).dt.days
    return orders