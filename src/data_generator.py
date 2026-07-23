import random
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

NUM_SUPPLIERS = 13
NUM_WAREHOUSES = 3


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


if __name__ == "__main__":
    suppliers_df = generate_suppliers()
    warehouses_df = generate_warehouses()

    suppliers_df.to_csv(DATA_DIR / "suppliers.csv", index=False)
    warehouses_df.to_csv(DATA_DIR / "warehouses.csv", index=False)

    print(suppliers_df)
    print(warehouses_df)