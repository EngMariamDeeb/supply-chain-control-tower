import random
import pandas as pd
from pathlib import Path
from datetime import date, timedelta

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

NUM_SUPPLIERS = 13
NUM_WAREHOUSES = 3
NUM_PRODUCTS = 20
NUM_CUSTOMERS = 25
NUM_ORDERS = 500
DESTINATIONS = ["Local", "Regional", "International"]
ORDER_DATE_START = date(2026, 1, 1)
ORDER_DATE_END = date(2026, 6, 30)
LEAD_TIME_RANGES = {
    "Local": (3, 5),
    "Regional": (6, 10),
    "International": (12, 20),
}

def generate_suppliers():
    suppliers = []
    for i in range(1, NUM_SUPPLIERS + 1):
        supplier = {
            "supplier_id": f"SUP-{i:03d}",
            "supplier_name": f"Supplier_{i:02d}",
            "reliability_score": round(random.uniform(0.5, 0.98), 2),
        }
        suppliers.append(supplier)
    return pd.DataFrame(suppliers)


def generate_warehouses():
    warehouses = []
    for i in range(1, NUM_WAREHOUSES + 1):
        warehouse = {
            "warehouse_id": f"WH-{i:03d}",
            "warehouse_name": f"Warehouse_{i:02d}",
            "congestion_level": round(random.uniform(0.1, 0.8), 2),
        }
        warehouses.append(warehouse)
    return pd.DataFrame(warehouses)


def generate_order_skeleton(suppliers_df, warehouses_df):
    supplier_ids = suppliers_df["supplier_id"].tolist()
    warehouse_ids = warehouses_df["warehouse_id"].tolist()
    product_ids = [f"PROD-{i:03d}" for i in range(1, NUM_PRODUCTS + 1)]
    customer_ids = [f"CUST-{i:03d}" for i in range(1, NUM_CUSTOMERS + 1)]

    orders = []
    for i in range(1, NUM_ORDERS + 1):
        order = {
            "order_id": f"ORD-{i:04d}",
            "product_id": random.choice(product_ids),
            "customer_id": random.choice(customer_ids),
            "supplier_id": random.choice(supplier_ids),
            "warehouse_id": random.choice(warehouse_ids),
            "destination": random.choice(DESTINATIONS),
        }
        orders.append(order)
    return pd.DataFrame(orders)


def compute_delay_risk(supplier_id, warehouse_id, destination, suppliers_df, warehouses_df):
    DESTINATION_RISK = {"Local": 0.1, "Regional": 0.3, "International": 0.5}

    reliability_score = suppliers_df.loc[
        suppliers_df["supplier_id"] == supplier_id, "reliability_score"
    ].iloc[0]
    congestion_level = warehouses_df.loc[
        warehouses_df["warehouse_id"] == warehouse_id, "congestion_level"
    ].iloc[0]

    supplier_risk = 1 - reliability_score
    warehouse_risk = congestion_level
    destination_risk = DESTINATION_RISK[destination]

    overall_delay_risk = (0.5 * supplier_risk) + (0.3 * warehouse_risk) + (0.2 * destination_risk)
    return round(overall_delay_risk, 4)


def generate_order_date():
    delta_days = (ORDER_DATE_END - ORDER_DATE_START).days
    random_offset = random.randint(0, delta_days)
    return ORDER_DATE_START + timedelta(days=random_offset)


def generate_expected_delivery_date(order_date, destination):
    """Add a destination-dependent lead time to the order date."""
    min_days, max_days = LEAD_TIME_RANGES[destination]
    lead_time = random.randint(min_days, max_days)
    return order_date + timedelta(days=lead_time)

if __name__ == "__main__":
    suppliers_df = generate_suppliers()
    warehouses_df = generate_warehouses()

    suppliers_df.to_csv(DATA_DIR / "suppliers.csv", index=False)
    warehouses_df.to_csv(DATA_DIR / "warehouses.csv", index=False)

    orders_df = generate_order_skeleton(suppliers_df, warehouses_df)

    orders_df["overall_delay_risk"] = orders_df.apply(
        lambda row: compute_delay_risk(
            row["supplier_id"], row["warehouse_id"], row["destination"],
            suppliers_df, warehouses_df
        ),
        axis=1
    )

    orders_df["order_date"] = [generate_order_date() for _ in range(len(orders_df))]
    orders_df["expected_delivery_date"] = orders_df.apply(
        lambda row: generate_expected_delivery_date(row["order_date"], row["destination"]),
        axis=1
    )

    orders_df["lead_time_days"] = (orders_df["expected_delivery_date"] - orders_df["order_date"]).dt.days

    print(orders_df[["order_date", "destination", "expected_delivery_date", "lead_time_days"]].head(10))
    print(orders_df.groupby("destination")["lead_time_days"].describe())
    print(orders_df.head(10))
    print(orders_df["overall_delay_risk"].describe())
