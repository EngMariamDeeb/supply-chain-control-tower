from pathlib import Path

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
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "orders.csv"

orders = load_orders(DATA_PATH)
orders = clean_orders(orders)

# KPIs
on_time_rate = calculate_on_time_rate(orders)
fill_rate = calculate_fill_rate(orders)
currently_delayed = count_currently_delayed(orders)
delivered_late = count_delivered_late(orders)
on_time_count = count_on_time_delivered(orders)

# Print summary
on_time_str = f"{on_time_rate:.1f}%" if on_time_rate is not None else "N/A"
fill_str = f"{fill_rate:.1f}%" if fill_rate is not None else "N/A"

print(f"On-Time Delivery Rate: {on_time_str}")
print(f"Fill Rate: {fill_str}")
print(f"Currently Delayed: {currently_delayed}")
print(f"Delivered Late: {delivered_late}")

# Chart
plot_on_time_vs_late(on_time_count, delivered_late)