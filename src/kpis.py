import pandas as pd


def calculate_on_time_rate(orders):
    delivered = orders[orders['order_status'] == 'Delivered']
    on_time = delivered[delivered['delivery_delay_days'] <= 0]
    rate = (len(on_time) / len(delivered)) * 100
    return rate

def calculate_fill_rate(orders):
    delivered = orders[orders['order_status'] == 'Delivered']
    total_ordered = delivered['quantity_ordered'].sum()
    total_delivered_units = delivered['quantity_delivered'].sum()
    rate = (total_delivered_units / total_ordered) * 100
    return rate

def count_currently_delayed(orders):
    return (orders['order_status'] == 'Delayed').sum()

def count_delivered_late(orders):
    delivered = orders[orders['order_status'] == 'Delivered']
    return (delivered['delivery_delay_days'] > 0).sum()
