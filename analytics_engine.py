import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from data_handler import load_and_clean_data, VALID_CITIES, VALID_CATEGORIES


def numpy_statistical_analysis():
    """Demonstrates 1D & 2D NumPy arrays, Indexing, Slicing, and core statistical functions."""
    df = load_and_clean_data()

    # 1D NumPy Arrays
    bills_1d = np.array(df["Total_Bill"])
    delivery_1d = np.array(df["Delivery_Mins"])

    # 2D NumPy Array (Columns: Price, Qty, Delivery_Mins, Rating)
    metrics_2d = df[["Price", "Qty", "Delivery_Mins", "Rating"]].to_numpy()

    print("\n================ NUMPY NUMERICAL ANALYSIS ================")
    print(f"1D Array Shape (Total_Bill) : {bills_1d.shape}")
    print(f"2D Array Shape (4 Metrics)  : {metrics_2d.shape}")

    # Indexing & Slicing
    print(f"\nIndexing (1st Order Bill)   : ₹{bills_1d[0]:.2f}")
    print(f"Slicing  (First 5 Bills)    : {bills_1d[:5]}")
    print(f"2D Slice (First 3 Orders - [Price, Qty, Del_Mins, Rating]):\n{metrics_2d[:3]}")

    # Statistical Functions: sum, mean, max, min, std
    print("\n--- Revenue & Bill Statistics (NumPy) ---")
    print(f"Total Revenue (Sum)         : ₹{np.sum(bills_1d):,.2f}")
    print(f"Average Order Value (Mean)  : ₹{np.mean(bills_1d):.2f}")
    print(f"Highest Single Bill (Max)   : ₹{np.max(bills_1d):.2f}")
    print(f"Lowest Single Bill (Min)    : ₹{np.min(bills_1d):.2f}")
    print(f"Bill Standard Deviation     : ₹{np.std(bills_1d):.2f}")

    print("\n--- Delivery Speed Statistics (NumPy) ---")
    print(f"Average Delivery Time       : {np.mean(delivery_1d):.2f} mins")
    print(f"Fastest Delivery (Min)      : {np.min(delivery_1d):.1f} mins")
    print(f"Slowest Delivery (Max)      : {np.max(delivery_1d):.1f} mins")
    print(f"Delivery Time Std Dev       : {np.std(delivery_1d):.2f} mins")
    print("==========================================================\n")


def pandas_groupby_analysis():
    """Performs Pandas GroupBy operations across Cities, Categories, and Payment Modes."""
    df = load_and_clean_data()

    city_summary = df.groupby("City").agg(
        Total_Orders=("Order_ID", "count"),
        Total_Revenue=("Total_Bill", "sum"),
        Avg_Delivery=("Delivery_Mins", "mean"),
        Avg_Rating=("Rating", "mean")
    ).round(2).sort_values(by="Total_Revenue", ascending=False)

    cat_summary = df.groupby("Category").agg(
        Units_Sold=("Qty", "sum"),
        Total_Revenue=("Total_Bill", "sum"),
        Avg_Rating=("Rating", "mean")
    ).round(2).sort_values(by="Total_Revenue", ascending=False)

    pay_counts = df["Payment_Mode"].value_counts()

    print("\n=============== PANDAS GROUPBY INSIGHTS ===============")
    print("\n1. CITY-WISE PERFORMANCE:")
    print(city_summary.to_string())

    print("\n2. CATEGORY-WISE SALES:")
    print(cat_summary.to_string())

    print("\n3. PAYMENT MODE BREAKDOWN:")
    for mode, count in pay_counts.items():
        print(f"   {mode:<6} : {count} orders")
    print("=======================================================\n")


def filter_and_sort_orders():
    """Interactive filtering (Late Deliveries / High-Value / By City) and sorting."""
    df = load_and_clean_data()
    print("\n--- FILTER & SORT OPTIONS ---")
    print("1. Show Top 10 Highest-Value Orders (Sorted)")
    print("2. Show Late Deliveries (> 40 mins)")
    print("3. Filter by Specific City")
    print("4. Filter by Specific Food Category")
    sub_ch = input("Choose filter (1-4): ").strip()

    cols = ["Order_ID", "Customer", "City", "Item", "Total_Bill", "Delivery_Mins", "Rating"]

    if sub_ch == "1":
        res = df.sort_values(by="Total_Bill", ascending=False).head(10)
        print("\n--- TOP 10 HIGHEST-VALUE ORDERS ---")
    elif sub_ch == "2":
        res = df[df["Delivery_Mins"] > 40].sort_values(by="Delivery_Mins", ascending=False)
        print(f"\n--- LATE DELIVERIES (>40 mins) | Total: {len(res)} ---")
    elif sub_ch == "3":
        print(f"Cities: {VALID_CITIES}")
        city = input("Enter City: ").strip()
        res = df[df["City"].str.lower() == city.lower()]
        print(f"\n--- ORDERS IN {city.upper()} | Total: {len(res)} ---")
    elif sub_ch == "4":
        print(f"Categories: {VALID_CATEGORIES}")
        cat = input("Enter Category: ").strip()
        res = df[df["Category"].str.lower() == cat.lower()]
        print(f"\n--- {cat.upper()} ORDERS | Total: {len(res)} ---")
    else:
        print("Invalid filter option!\n")
        return

    print("No matching records found.\n" if res.empty else res[cols].to_string(index=False) + "\n")


def generate_summary_report():
    """Displays full statistical describe() summary and saves delivery_report.txt."""
    df = load_and_clean_data()

    total_rev = np.sum(df["Total_Bill"])
    late_count = len(df[df["Delivery_Status"] == "Late"])
    top_city = df.groupby("City")["Total_Bill"].sum().idxmax()
    top_item = df.groupby("Item")["Qty"].sum().idxmax()
    desc_table = df[["Price", "Qty", "Total_Bill", "Delivery_Mins", "Rating"]].describe().round(2)

    report_text = (
        "==================================================\n"
        "     FOOD DELIVERY SALES & OPERATIONS REPORT\n"
        "==================================================\n"
        f"Total Orders Processed   : {len(df)}\n"
        f"Total Revenue (incl GST) : ₹{total_rev:,.2f}\n"
        f"Average Order Value      : ₹{np.mean(df['Total_Bill']):.2f}\n"
        f"Top Performing City      : {top_city}\n"
        f"Most Ordered Dish        : {top_item}\n"
        f"Late Deliveries (>40m)   : {late_count} ({(late_count/len(df))*100:.1f}%)\n\n"
        "--- PANDAS STATISTICAL SUMMARY (df.describe()) ---\n"
        f"{desc_table.to_string()}\n"
        "==================================================\n"
    )

    print("\n" + report_text)

    # File Handling: Export report to text file
    with open("delivery_report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)
    print("Full summary report saved to 'delivery_report.txt'!\n")


def show_visual_dashboard():
    """Plots a 2-chart Matplotlib dashboard: City Revenue & Category Revenue."""
    df = load_and_clean_data()

    city_rev = df.groupby("City")["Total_Bill"].sum().sort_values(ascending=False)
    cat_rev = df.groupby("Category")["Total_Bill"].sum().sort_values(ascending=False)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Chart 1: City-wise Revenue (Top City highlighted in crimson)
    max_city = city_rev.max()
    c_colors = ["crimson" if v == max_city else "royalblue" for v in city_rev]
    axes[0].bar(city_rev.index, city_rev.values, color=c_colors, edgecolor="black")
    axes[0].set_title("City-Wise Total Revenue (Red = Top City)")
    axes[0].set_xlabel("City")
    axes[0].set_ylabel("Revenue (₹)")
    axes[0].tick_params(axis="x", rotation=15)

    # Chart 2: Category-wise Revenue
    axes[1].bar(cat_rev.index, cat_rev.values, color="darkorange", edgecolor="black")
    axes[1].set_title("Food Category-Wise Total Revenue")
    axes[1].set_xlabel("Category")
    axes[1].set_ylabel("Revenue (₹)")
    axes[1].tick_params(axis="x", rotation=15)

    plt.tight_layout()
    plt.show()