import pandas as pd


def calculate_warehouse_on_time_rate(orders):
    resolved = orders[orders['order_status'].isin(['Delivered', 'Delayed'])]
    summary = resolved.groupby('warehouse_id')['order_status'].agg(
        total='count',
        on_time=lambda s: (s == 'Delivered').sum(),
        late=lambda s: (s == 'Delayed').sum()
    ).reset_index()
    summary['on_time_rate'] = (summary['on_time'] / summary['total']) * 100
    return summary


if __name__ == "__main__":
    from pathlib import Path
    import sys
    sys.path.append(str(Path(__file__).resolve().parent.parent))

    from data_loader import load_orders
    from data_cleaning import clean_orders

    orders = load_orders(Path(__file__).resolve().parent.parent.parent / "data" / "orders.csv")
    orders = clean_orders(orders)

    print(calculate_warehouse_on_time_rate(orders))