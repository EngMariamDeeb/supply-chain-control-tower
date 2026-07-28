import matplotlib.pyplot as plt

def plot_on_time_vs_late(on_time_count, late_count):
    categories = ['On Time', 'Late']
    counts = [on_time_count, late_count]
    plt.bar(categories, counts, color=['green', 'red'])
    plt.title('On-Time vs. Late Deliveries')
    plt.xlabel('Delivery Status')
    plt.ylabel('Number of Orders')
    plt.show()


def plot_supplier_on_time_rate(supplier_summary):
    sorted_summary = supplier_summary.sort_values('on_time_rate', ascending=False)
    plt.figure(figsize=(8, 6))
    plt.barh(sorted_summary['supplier_id'], sorted_summary['on_time_rate'], color='steelblue')
    plt.title('Supplier On-Time Rate (Worst to Best, Top to Bottom)')
    plt.xlabel('On-Time Rate (%)')
    plt.ylabel('Supplier')
    plt.tight_layout()
    plt.show()


def plot_warehouse_on_time_rate(warehouse_summary):
    """Bar chart of on-time rate per warehouse, best to worst."""
    sorted_summary = warehouse_summary.sort_values('on_time_rate', ascending=False)
    plt.bar(sorted_summary['warehouse_id'], sorted_summary['on_time_rate'], color='darkorange')
    plt.title('Warehouse On-Time Rate')
    plt.xlabel('Warehouse')
    plt.ylabel('On-Time Rate (%)')
    plt.show()