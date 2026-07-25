import pandas as pd

REQUIRED_COLUMNS = [
    "order_id", "product_id", "customer_id", "supplier_id", "warehouse_id",
    "destination", "quantity_ordered", "quantity_delivered",
    "order_date", "expected_delivery_date", "actual_delivery_date", "order_status"
]


def load_orders(filepath):
    try:
        orders = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Could not find orders file at '{filepath}'. "
            f"Check the path is correct, or run data_generator.py to create it."
        )
    except pd.errors.EmptyDataError:
        raise ValueError(f"The file at '{filepath}' exists but is empty.")

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in orders.columns]
    if missing_columns:
        raise ValueError(
            f"orders.csv is missing expected column(s): {missing_columns}. "
            f"Check the file matches the current schema."
        )

    return orders
