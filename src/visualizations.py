import pandas as pd
import matplotlib.pyplot as plt

def plot_on_time_vs_late(on_time_count, late_count):
    categories = ['On Time', 'Late']
    counts = [on_time_count, late_count]
    plt.bar(categories, counts, color=['green', 'red'])
    plt.title('On-Time vs. Late Deliveries')
    plt.xlabel('Delivery Status')
    plt.ylabel('Number of Orders')
    plt.show()
    