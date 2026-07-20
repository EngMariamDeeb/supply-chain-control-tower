import pandas as pd

def load_orders(filepath):
    orders= pd.read_csv(filepath)
    return orders
