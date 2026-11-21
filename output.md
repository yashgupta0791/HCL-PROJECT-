# Sample Execution Outputs — Food Delivery & Restaurant Sales Analyser

**Student Name:** Yash Kumar Gupta  
**Admission No.:** 2026B01010947  
**Course & Section:** B.Tech CSE (Semester 1) — CSE 15  
**GitHub Repository:** https://github.com/yashgupta0791/HCL-PROJECT-

---

## Main Menu Interface
```text
Dataset 'food_orders.csv' created automatically with 60 records!

==========================================================
     FOOD DELIVERY & RESTAURANT SALES ANALYSER (v1.0)
     Built with Python, NumPy, Pandas & Matplotlib
==========================================================
-------------------- MAIN MENU --------------------
  1. Display All Orders (60+ Records)
  2. Add New Order
  3. Search Order (by ID, Customer, or City)
  4. Update Existing Order
  5. Delete Order
  6. NumPy Statistical Analysis (1D/2D & Slicing)
  7. Pandas GroupBy Insights (City / Category / Pay)
  8. Filter & Sort Orders (Top 10 / Late / City)
  9. Generate & Export Summary Report (.txt)
 10. Show Visual Sales Dashboard (2 Graphs)
 11. Exit
---------------------------------------------------
Enter your choice (1-11):
```

---

## Option 1: Display All Orders (Sample of 60 Records)
```text
Enter your choice (1-11): 1

========== ALL FOOD DELIVERY ORDERS (Total: 60) ==========
 Order_ID Customer      City                 Item  Qty  Total_Bill  Delivery_Mins Delivery_Status  Rating Payment_Mode
     5001    Aarav     Delhi Paneer Butter Masala    4      1092.0           29.0         On-Time     4.1          UPI
     5002    Priya     Noida    Dal Makhani Combo    4       924.0           41.0            Late     3.3         Card
     5003    Rohan Ghaziabad        Chole Bhature    4       588.0           27.0         On-Time     4.7         Cash
     5004    Sneha  Gurugram   Cheese Burst Pizza    1       336.0           58.0            Late     3.5          UPI
     5005    Kabir   Lucknow      Veg Burger Meal    1       189.0           18.0         On-Time     4.8         Card
     5006   Ananya     Delhi          Masala Dosa    1       157.5           37.5         On-Time     3.7         Cash
     5007    Vikas     Noida          Idli Sambar    2       231.0           37.0         On-Time     4.6          UPI
     5008     Neha Ghaziabad        Hakka Noodles    1       199.5           47.0            Late     4.2         Card
     5009      Dev  Gurugram       Veg Manchurian    3       661.5           26.0         On-Time     4.5         Cash
     5010    Pooja   Lucknow          Cold Coffee    3       409.5           28.0         On-Time     4.4          UPI
... (remaining 50 rows displayed up to Order_ID 5060)
=================================================================
```
*(Note: Blank values in `Delivery_Mins` and `Rating` are automatically imputed using the column median `37.5` and mean `4.0`.)*

---

## Option 2: Add New Order
```text
Enter your choice (1-11): 2
Enter New Order ID (e.g., 5061): 5061
Enter Customer Name: Rahul
Available Cities: ('Delhi', 'Noida', 'Ghaziabad', 'Gurugram', 'Lucknow')
Enter City: Noida
Enter Item Name (exact spelling): Cheese Burst Pizza
Enter Quantity: 2
Enter Delivery Time (in mins): 32
Enter Customer Rating (1.0 - 5.0): 4.7
Payment Modes: ('UPI', 'Card', 'Cash')
Enter Payment Mode: UPI

Order #5061 for Rahul added successfully!
```

---

## Option 3: Search Order (by City = Noida)
```text
Enter your choice (1-11): 3
Search by Order ID, Customer Name, or City: Noida

--- SEARCH RESULTS (12 found) ---
 Order_ID Customer  City              Item  Total_Bill  Delivery_Mins  Rating
     5002    Priya Noida Dal Makhani Combo       924.0           41.0     3.3
     5007    Vikas Noida       Idli Sambar       231.0           37.0     4.6
     5012    Meera Noida Dal Makhani Combo       924.0           27.0     3.4
     5017    Tanvi Noida       Idli Sambar       115.5           36.0     3.7
     5022   Manish Noida Dal Makhani Combo       231.0           37.0     4.7
     5027   Shruti Noida       Idli Sambar       346.5           55.0     3.4
```

---

## Option 4: Update Existing Order
```text
Enter your choice (1-11): 4
Enter Order ID to update: 5004
Found Order #5004 | Customer: Sneha | Item: Cheese Burst Pizza
Current Delivery Time: 58.0 mins | Current Rating: 3.5
Enter New Quantity: 2
Enter New Delivery Time (mins): 35
Enter New Rating (1.0 - 5.0): 4.5
Order #5004 updated successfully!
```

---

## Option 5: Delete Order
```text
Enter your choice (1-11): 5
Enter Order ID to delete: 5061
Deleted Order #5061 (Customer: Rahul) successfully!
```

---

## Option 6: NumPy Statistical Analysis (1D/2D Arrays, Indexing & Slicing)
```text
Enter your choice (1-11): 6

================ NUMPY NUMERICAL ANALYSIS ================
1D Array Shape (Total_Bill) : (60,)
2D Array Shape (4 Metrics)  : (60, 4)

Indexing (1st Order Bill)   : ₹1092.00
Slicing  (First 5 Bills)    : [1092.  924.  588.  336.  189.]
2D Slice (First 3 Orders - [Price, Qty, Del_Mins, Rating]):
[[260.    4.   29.    4.1]
 [220.    4.   41.    3.3]
 [140.    4.   27.    4.7]]

--- Revenue & Bill Statistics (NumPy) ---
Total Revenue (Sum)         : ₹32,413.50
Average Order Value (Mean)  : ₹540.23
Highest Single Bill (Max)   : ₹1344.00
Lowest Single Bill (Min)    : ₹115.50
Bill Standard Deviation     : ₹332.02

--- Delivery Speed Statistics (NumPy) ---
Average Delivery Time       : 39.05 mins
Fastest Delivery (Min)      : 18.0 mins
Slowest Delivery (Max)      : 61.0 mins
Delivery Time Std Dev       : 11.55 mins
==========================================================
```

---

## Option 7: Pandas GroupBy Insights
```text
Enter your choice (1-11): 7

=============== PANDAS GROUPBY INSIGHTS ===============

1. CITY-WISE PERFORMANCE:
           Total_Orders  Total_Revenue  Avg_Delivery  Avg_Rating
City                                                            
Gurugram             12         9345.0         46.08        4.03
Delhi                12         8568.0         37.96        3.97
Noida                12         5197.5         41.00        3.88
Ghaziabad            12         4798.5         37.29        3.98
Lucknow              12         4504.5         32.92        4.18

2. CATEGORY-WISE SALES:
              Units_Sold  Total_Revenue  Avg_Rating
Category                                           
North Indian          53        11865.0        3.85
Fast Food             29         7833.0        4.11
Chinese               31         6562.5        3.92
South Indian          29         4105.5        4.14
Beverages             15         2047.5        4.20

3. PAYMENT MODE BREAKDOWN:
   UPI    : 20 orders
   Card   : 20 orders
   Cash   : 20 orders
=======================================================
```

---

## Option 8: Filter & Sort Orders (Top 10 Highest-Value Orders)
```text
Enter your choice (1-11): 8

--- FILTER & SORT OPTIONS ---
1. Show Top 10 Highest-Value Orders (Sorted)
2. Show Late Deliveries (> 40 mins)
3. Filter by Specific City
4. Filter by Specific Food Category
Choose filter (1-4): 1

--- TOP 10 HIGHEST-VALUE ORDERS ---
 Order_ID Customer     City                 Item  Total_Bill  Delivery_Mins  Rating
     5034    Sneha Gurugram   Cheese Burst Pizza      1344.0           55.0     4.2
     5014    Karan Gurugram   Cheese Burst Pizza      1344.0           53.0     4.2
     5001    Aarav    Delhi Paneer Butter Masala      1092.0           29.0     4.1
     5011    Arjun    Delhi Paneer Butter Masala      1092.0           41.0     3.1
     5041    Arjun    Delhi Paneer Butter Masala      1092.0           48.0     3.9
     5031    Aarav    Delhi Paneer Butter Masala      1092.0           37.0     4.9
     5044    Karan Gurugram   Cheese Burst Pizza      1008.0           31.0     4.9
     5054     Yash Gurugram   Cheese Burst Pizza      1008.0           32.0     4.2
     5002    Priya    Noida    Dal Makhani Combo       924.0           41.0     3.3
     5012    Meera    Noida    Dal Makhani Combo       924.0           27.0     3.4
```

---

## Option 9: Summary Report & File Export (`delivery_report.txt`)
```text
Enter your choice (1-11): 9

==================================================
     FOOD DELIVERY SALES & OPERATIONS REPORT
==================================================
Total Orders Processed   : 60
Total Revenue (incl GST) : ₹32,413.50
Average Order Value      : ₹540.23
Top Performing City      : Gurugram
Most Ordered Dish        : Paneer Butter Masala
Late Deliveries (>40m)   : 25 (41.7%)

--- PANDAS STATISTICAL SUMMARY (df.describe()) ---
        Price    Qty  Total_Bill  Delivery_Mins  Rating
count   60.00  60.00       60.00          60.00   60.00
mean   191.00   2.62      540.22          39.05    4.01
std     61.58   1.21      334.82          11.64    0.52
min    110.00   1.00      115.50          18.00    3.00
25%    140.00   1.00      231.00          29.75    3.68
50%    185.00   3.00      425.25          37.50    4.00
75%    220.00   4.00      766.50          47.00    4.40
max    320.00   4.00     1344.00          61.00    5.00
==================================================

Full summary report saved to 'delivery_report.txt'!
```

---

## Option 10: Visual Sales Dashboard (Matplotlib)
Running Option `10` opens a side-by-side Matplotlib dashboard:
* **Left Chart (City-Wise Total Revenue):** Highlights **Gurugram (₹9,345.00)** in crimson as the top city, followed by Delhi (₹8,568.00), Noida (₹5,197.50), Ghaziabad (₹4,798.50), and Lucknow (₹4,504.50).
* **Right Chart (Category-Wise Total Revenue):** Compares **North Indian (₹11,865.00)**, Fast Food (₹7,833.00), Chinese (₹6,562.50), South Indian (₹4,105.50), and Beverages (₹2,047.50).