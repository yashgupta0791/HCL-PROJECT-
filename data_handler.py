import os
import csv
import numpy as np
import pandas as pd

CSV_FILE = "food_orders.csv"

# 1. TUPLES: Fixed allowed values
VALID_CITIES = ("Delhi", "Noida", "Ghaziabad", "Gurugram", "Lucknow")
VALID_CATEGORIES = ("North Indian", "Fast Food", "South Indian", "Chinese", "Beverages")
PAYMENT_MODES = ("UPI", "Card", "Cash")

# 2. DICTIONARY: Sample menu items mapped to (Category, Base Price in ₹)
MENU_CATALOG = {
    "Paneer Butter Masala": ("North Indian", 260),
    "Dal Makhani Combo": ("North Indian", 220),
    "Chole Bhature": ("North Indian", 140),
    "Cheese Burst Pizza": ("Fast Food", 320),
    "Veg Burger Meal": ("Fast Food", 180),
    "Masala Dosa": ("South Indian", 150),
    "Idli Sambar": ("South Indian", 110),
    "Hakka Noodles": ("Chinese", 190),
    "Veg Manchurian": ("Chinese", 210),
    "Cold Coffee": ("Beverages", 130),
}


def create_dataset():
    """Creates a 60-record food delivery dataset CSV if it does not exist."""
    if os.path.exists(CSV_FILE):
        return

    np.random.seed(101)
    customer_names = [
        "Aarav", "Priya", "Rohan", "Sneha", "Kabir", "Ananya", "Vikas", "Neha", "Dev", "Pooja",
        "Arjun", "Meera", "Sahil", "Karan", "Riya", "Aditya", "Tanvi", "Harsh", "Simran", "Nikhil",
        "Ishita", "Manish", "Divya", "Yash", "Kriti", "Gaurav", "Shruti", "Pranav", "Sakshi", "Abhishek"
    ]
    item_list = list(MENU_CATALOG.keys())

    headers = [
        "Order_ID", "Customer", "City", "Item", "Category",
        "Price", "Qty", "Delivery_Mins", "Rating", "Payment_Mode"
    ]

    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for i in range(60):
            order_id = 5001 + i
            cust = customer_names[i % len(customer_names)]
            city = VALID_CITIES[i % len(VALID_CITIES)]
            item = item_list[i % len(item_list)]
            category, price = MENU_CATALOG[item]
            qty = int(np.random.randint(1, 5))

            # Intentional missing values in 3 rows to demonstrate Pandas missing-data handling
            del_mins = "" if i in (5, 22) else int(np.random.randint(18, 62))
            rating = "" if i in (12, 37) else round(float(np.random.uniform(3.0, 5.0)), 1)
            pay_mode = PAYMENT_MODES[i % len(PAYMENT_MODES)]

            writer.writerow([order_id, cust, city, item, category, price, qty, del_mins, rating, pay_mode])

    print(f"Dataset '{CSV_FILE}' created automatically with 60 records!\n")


def load_and_clean_data():
    """Reads CSV into Pandas DataFrame, handles missing values, and computes derived columns."""
    df = pd.read_csv(CSV_FILE)

    # Handle Missing Values: fill blank Delivery_Mins with median & Rating with mean
    if df["Delivery_Mins"].isnull().sum() > 0:
        df["Delivery_Mins"] = df["Delivery_Mins"].fillna(round(df["Delivery_Mins"].median(), 1))
    if df["Rating"].isnull().sum() > 0:
        df["Rating"] = df["Rating"].fillna(round(df["Rating"].mean(), 1))

    # Vectorized NumPy calculations for Total Bill (including 5% GST) and Delivery Status
    prices = np.array(df["Price"])
    qtys = np.array(df["Qty"])
    del_times = np.array(df["Delivery_Mins"])

    subtotal = prices * qtys
    df["Total_Bill"] = np.round(subtotal * 1.05, 2)  # 5% GST included
    df["Delivery_Status"] = np.where(del_times <= 40, "On-Time", "Late")
    return df


def save_data(df):
    """Saves the base columns back to food_orders.csv."""
    base_cols = [
        "Order_ID", "Customer", "City", "Item", "Category",
        "Price", "Qty", "Delivery_Mins", "Rating", "Payment_Mode"
    ]
    df[base_cols].to_csv(CSV_FILE, index=False)


def display_all_orders():
    """Displays selected columns of all orders cleanly in the VS Code terminal."""
    df = load_and_clean_data()
    cols = [
        "Order_ID", "Customer", "City", "Item", "Qty",
        "Total_Bill", "Delivery_Mins", "Delivery_Status", "Rating", "Payment_Mode"
    ]
    print(f"\n========== ALL FOOD DELIVERY ORDERS (Total: {len(df)}) ==========")
    print(df[cols].to_string(index=False))
    print("=" * 65 + "\n")


def add_order():
    """Adds a new order using Set (unique ID check), Tuple validation, and Dictionary."""
    df = load_and_clean_data()
    existing_ids = set(df["Order_ID"])  # SET for duplicate Order_ID prevention

    try:
        order_id = int(input("Enter New Order ID (e.g., 5061): ").strip())
        if order_id in existing_ids:
            print("Error: Order ID already exists!\n")
            return

        customer = input("Enter Customer Name: ").strip()
        print(f"Available Cities: {VALID_CITIES}")
        city = input("Enter City: ").strip()
        if city not in VALID_CITIES:
            print("Error: Please select a valid city from the list.\n")
            return

        print("\n--- Quick Menu ---")
        for name, (cat, pr) in MENU_CATALOG.items():
            print(f"  {name:<22} ({cat:<12}) - ₹{pr}")
        item = input("\nEnter Item Name (exact spelling): ").strip()

        if item in MENU_CATALOG:
            category, price = MENU_CATALOG[item]
        else:
            print(f"Custom item detected. Valid Categories: {VALID_CATEGORIES}")
            category = input("Enter Category: ").strip()
            if category not in VALID_CATEGORIES:
                print("Error: Invalid category!\n")
                return
            price = float(input("Enter Unit Price (₹): "))

        qty = int(input("Enter Quantity: "))
        del_mins = float(input("Enter Delivery Time (in mins): "))
        rating = float(input("Enter Customer Rating (1.0 - 5.0): "))

        print(f"Payment Modes: {PAYMENT_MODES}")
        pay_mode = input("Enter Payment Mode: ").strip()
        if pay_mode not in PAYMENT_MODES:
            print("Error: Invalid payment mode!\n")
            return

        new_order = {
            "Order_ID": order_id, "Customer": customer, "City": city,
            "Item": item, "Category": category, "Price": price,
            "Qty": qty, "Delivery_Mins": del_mins, "Rating": rating,
            "Payment_Mode": pay_mode
        }

        df = pd.concat([df, pd.DataFrame([new_order])], ignore_index=True)
        save_data(df)
        print(f"\nOrder #{order_id} for {customer} added successfully!\n")

    except ValueError:
        print("Invalid numeric input! Order cancelled.\n")


def search_order():
    """Searches orders by Order_ID, Customer Name, or City."""
    df = load_and_clean_data()
    query = input("Search by Order ID, Customer Name, or City: ").strip()

    if query.isdigit():
        result = df[df["Order_ID"] == int(query)]
    else:
        mask = (
            df["Customer"].str.lower().str.contains(query.lower()) |
            df["City"].str.lower().str.contains(query.lower())
        )
        result = df[mask]

    if result.empty:
        print(f"\nNo records found matching '{query}'.\n")
    else:
        cols = ["Order_ID", "Customer", "City", "Item", "Total_Bill", "Delivery_Mins", "Rating"]
        print(f"\n--- SEARCH RESULTS ({len(result)} found) ---")
        print(result[cols].to_string(index=False))
        print()


def update_order():
    """Updates Delivery Time and Customer Rating for an existing Order_ID."""
    df = load_and_clean_data()
    try:
        oid = int(input("Enter Order ID to update: ").strip())
        if oid not in df["Order_ID"].values:
            print(f"Order ID {oid} not found!\n")
            return

        idx = df.index[df["Order_ID"] == oid][0]
        print(f"Found Order #{oid} | Customer: {df.loc[idx, 'Customer']} | Item: {df.loc[idx, 'Item']}")
        print(f"Current Delivery Time: {df.loc[idx, 'Delivery_Mins']} mins | Current Rating: {df.loc[idx, 'Rating']}")

        df.loc[idx, "Qty"] = int(input("Enter New Quantity: "))
        df.loc[idx, "Delivery_Mins"] = float(input("Enter New Delivery Time (mins): "))
        df.loc[idx, "Rating"] = float(input("Enter New Rating (1.0 - 5.0): "))

        save_data(df)
        print(f"Order #{oid} updated successfully!\n")
    except ValueError:
        print("Invalid numeric input! Update cancelled.\n")


def delete_order():
    """Deletes an order record permanently by Order_ID."""
    df = load_and_clean_data()
    try:
        oid = int(input("Enter Order ID to delete: ").strip())
        if oid not in df["Order_ID"].values:
            print(f"Order ID {oid} not found!\n")
            return

        cust = df.loc[df["Order_ID"] == oid, "Customer"].values[0]
        df = df[df["Order_ID"] != oid]
        save_data(df)
        print(f"Deleted Order #{oid} (Customer: {cust}) successfully!\n")
    except ValueError:
        print("Invalid Order ID!\n")