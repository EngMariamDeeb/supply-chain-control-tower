from data_loader import load_orders
from data_cleaning import clean_orders
from kpis import (
    calculate_on_time_rate,
    calculate_fill_rate,
    count_currently_delayed,
    count_delivered_late,
    count_on_time_delivered,
)
from visualizations import plot_on_time_vs_late

# Load and clean the data
orders = load_orders('data/orders.csv')
orders = clean_orders(orders)

# KPIs
on_time_rate = calculate_on_time_rate(orders)
fill_rate = calculate_fill_rate(orders)
currently_delayed = count_currently_delayed(orders)
delivered_late = count_delivered_late(orders)
on_time_count = count_on_time_delivered(orders)

# Print summary
print(f"On-Time Delivery Rate: {on_time_rate:.1f}%")
print(f"Fill Rate: {fill_rate:.1f}%")
print(f"Currently Delayed: {currently_delayed}")
print(f"Delivered Late: {delivered_late}")

# Chart
plot_on_time_vs_late(on_time_count, delivered_late)