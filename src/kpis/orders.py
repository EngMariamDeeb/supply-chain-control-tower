import pandas as pd


def calculate_average_lead_time(orders):
    """Average number of days between order_date and expected_delivery_date,
    across all orders regardless of status."""
    lead_times = (orders['expected_delivery_date'] - orders['order_date']).dt.days
    return lead_times.mean()


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

if __name__ == "__main__":
    from pathlib import Path
    import sys
    sys.path.append(str(Path(__file__).resolve().parent.parent))

    from data_loader import load_orders
    from data_cleaning import clean_orders

    orders = load_orders(Path(__file__).resolve().parent.parent.parent / "data" / "orders.csv")
    orders = clean_orders(orders)

    print(f"Average Lead Time: {calculate_average_lead_time(orders):.1f} days")
    print(f"On-Time Rate: {calculate_on_time_rate(orders):.1f}%")
    print(f"Fill Rate: {calculate_fill_rate(orders):.1f}%")
    print(f"Currently Delayed: {count_currently_delayed(orders)}")
    print(f"Delivered Late: {count_delivered_late(orders)}")
    print(f"On-Time Delivered: {count_on_time_delivered(orders)}")