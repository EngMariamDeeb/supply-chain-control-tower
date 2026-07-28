from pathlib import Path

from data_loader import load_orders
from data_cleaning import clean_orders
from kpis.orders import (
    calculate_average_lead_time,
    calculate_on_time_rate,
    calculate_fill_rate,
    count_delivered_late,
    count_on_time_delivered,
)
from kpis.supplier import calculate_supplier_reliability
from kpis.warehouse import calculate_warehouse_on_time_rate
from visualizations import (
    plot_on_time_vs_late,
    plot_supplier_on_time_rate,
    plot_warehouse_on_time_rate,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "orders.csv"


def run():
    # Load and clean the data
    orders = load_orders(DATA_PATH)
    orders = clean_orders(orders)

    # KPIs
    average_lead_time = calculate_average_lead_time(orders)
    on_time_rate = calculate_on_time_rate(orders)
    fill_rate = calculate_fill_rate(orders)
    delivered_late = count_delivered_late(orders)
    on_time_count = count_on_time_delivered(orders)
    supplier_summary = calculate_supplier_reliability(orders)
    warehouse_summary = calculate_warehouse_on_time_rate(orders)

    # Print summary
    average_lead_time_str = f"{average_lead_time:.1f} days" if average_lead_time is not None else "N/A"
    on_time_str = f"{on_time_rate:.1f}%" if on_time_rate is not None else "N/A"
    fill_str = f"{fill_rate:.1f}%" if fill_rate is not None else "N/A"

    print(f"Average Lead Time: {average_lead_time_str}")
    print(f"On-Time Delivery Rate: {on_time_str}")
    print(f"Fill Rate: {fill_str}")
    print(f"Delivered Late: {delivered_late}")
    print("\nSupplier On-Time Summary:")
    print(supplier_summary)
    print("\nWarehouse On-Time Summary:")
    print(warehouse_summary)

    # Charts
    plot_on_time_vs_late(on_time_count, delivered_late)
    plot_supplier_on_time_rate(supplier_summary)
    plot_warehouse_on_time_rate(warehouse_summary)


if __name__ == "__main__":
    run()