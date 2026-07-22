import pandas as pd


def calculate_on_time_rate(orders):
    delivered = orders[orders['order_status'] == 'Delivered']
    if len(delivered) == 0:
        return None
    on_time = delivered[delivered['delivery_delay_days'] <= 0]
    return (len(on_time) / len(delivered)) * 100

def calculate_fill_rate(orders):
    delivered = orders[orders['order_status'] == 'Delivered']
    total_ordered = delivered['quantity_ordered'].sum()
    if total_ordered == 0:
        return None
    total_delivered_units = delivered['quantity_delivered'].sum()
    return (total_delivered_units / total_ordered) * 100

def count_currently_delayed(orders):
    return (orders['order_status'] == 'Delayed').sum()

def count_delivered_late(orders):
    delivered = orders[orders['order_status'] == 'Delivered']
    return (delivered['delivery_delay_days'] > 0).sum()

def count_on_time_delivered(orders):
    delivered = orders[orders['order_status'] == 'Delivered']
    return (delivered['delivery_delay_days'] <= 0).sum()