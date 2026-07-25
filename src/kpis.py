import pandas as pd


def calculate_on_time_rate(orders):
    resolved = orders[orders['order_status'].isin(['Delivered', 'Delayed'])]
    if len(resolved) == 0:
        return None
    on_time = resolved[resolved['order_status'] == 'Delivered']
    return (len(on_time) / len(resolved)) * 100


def calculate_fill_rate(orders):
    fulfilled = orders[orders['order_status'].isin(['Delivered', 'Delayed'])]
    total_ordered = fulfilled['quantity_ordered'].sum()
    if total_ordered == 0:
        return None
    total_delivered_units = fulfilled['quantity_delivered'].sum()
    return (total_delivered_units / total_ordered) * 100


def count_currently_delayed(orders):
    return (orders['order_status'] == 'Delayed').sum()


def count_delivered_late(orders):
    return (orders['order_status'] == 'Delayed').sum()


def count_on_time_delivered(orders):
    return (orders['order_status'] == 'Delivered').sum()