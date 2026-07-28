import pandas as pd


def calculate_supplier_reliability(orders):
    resolved = orders[orders['order_status'].isin(['Delivered', 'Delayed'])]
    summary = resolved.groupby('supplier_id')['order_status'].agg(
        total='count',
        on_time=lambda s: (s == 'Delivered').sum(),
        late=lambda s: (s == 'Delayed').sum()
    ).reset_index()
    summary['on_time_rate'] = (summary['on_time'] / summary['total']) * 100
    return summary


def calculate_supplier_fill_rate(orders):
    """Return a per-supplier breakdown of fill performance:
    supplier_id, total quantity ordered, total quantity delivered, fill rate (%)"""
    fulfilled = orders[orders['order_status'].isin(['Delivered', 'Delayed'])]

    summary = fulfilled.groupby('supplier_id').agg(
        total_ordered=('quantity_ordered', 'sum'),
        total_delivered=('quantity_delivered', 'sum')
    ).reset_index()

    summary['fill_rate'] = (summary['total_delivered'] / summary['total_ordered']) * 100
    return summary


if __name__ == "__main__":
    from pathlib import Path
    import sys
    sys.path.append(str(Path(__file__).resolve().parent.parent))

    from data_loader import load_orders
    from data_cleaning import clean_orders

    orders = load_orders(Path(__file__).resolve().parent.parent.parent / "data" / "orders.csv")
    orders = clean_orders(orders)

    print(calculate_supplier_reliability(orders))
    print(calculate_supplier_fill_rate(orders))