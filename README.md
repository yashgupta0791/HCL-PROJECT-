# Food Delivery & Restaurant Sales Analyser

A modular, menu-driven Python data analytics project built for the **HCL Tech Classroom Training Program (B.Tech CSE – Semester 1)**. It manages food delivery orders across Indian cities, cleans missing data, computes GST-inclusive billing and delivery speed metrics, performs statistical analysis using **NumPy** and **Pandas**, exports summary reports, and renders a dual-chart sales dashboard using **Matplotlib**.

---

## Key Features
* **Auto-Generated 60-Record Dataset:** Automatically creates `food_orders.csv` with 60 realistic food delivery orders across 5 cities (Delhi, Noida, Ghaziabad, Gurugram, Lucknow) and 5 food categories, including intentional blank values to demonstrate missing-data handling.
* **Complete CRUD Operations:**
  * Display all orders with calculated **Total Bill (incl. 5% GST)** and **On-Time / Late** status.
  * Add new orders (uses a Python `Set` to block duplicate Order IDs and `Tuples` to validate Cities, Categories, and Payment Modes).
  * Search orders by Order ID, Customer Name, or City.
  * Update existing order Quantity, Delivery Time, and Rating.
  * Delete orders permanently by Order ID.
* **NumPy Statistical Analysis:** 1D and 2D array creation, indexing, slicing, and core statistics (`sum`, `mean`, `max`, `min`, `std`) for revenue and delivery speed.
* **Pandas Data Analysis:** CSV I/O, missing-value imputation (`fillna` with median/mean), interactive filtering & sorting (Top 10 orders, Late deliveries `> 40 mins`, City/Category filters), multi-metric `groupby()` aggregations, and `describe()`.
* **File Handling:** Reads/writes `food_orders.csv` and exports a formatted operations report to `delivery_report.txt`.
* **Visual Sales Dashboard:** Plots a 2-chart Matplotlib dashboard comparing **City-Wise Total Revenue** (top city highlighted in red) and **Category-Wise Total Revenue**.

---

## Project Structure
```text
├── main.py                # Main entry point & 11-option interactive menu
├── data_handler.py        # Dataset generator, missing-value cleaning & CRUD operations
├── analytics_engine.py    # NumPy stats, Pandas GroupBy/filters, report export & graphs
├── food_orders.csv        # Auto-generated 60-record dataset
├── delivery_report.txt    # Auto-generated summary report (created via Option 9)
└── README.md              # Project documentation
```

---

## Syllabus & Technical Parameters Covered

| Parameter | Implementation in Project |
| :--- | :--- |
| **Dataset Creation** | 60-record CSV dataset (`food_orders.csv`) auto-generated on first run. |
| **Python Data Structures** | `Tuple` (`VALID_CITIES`, `VALID_CATEGORIES`, `PAYMENT_MODES`), `Dictionary` (`MENU_CATALOG`, new order record), `List` (`customer_names`), `Set` (`existing_ids`). |
| **User-Defined Functions** | 15+ modular functions across 3 Python files. |
| **Python Modules** | 3 separate modules (`main.py` imports `data_handler.py` and `analytics_engine.py`). |
| **NumPy** | 1D arrays (`bills_1d`, `delivery_1d`), 2D array (`metrics_2d`), indexing, slicing, `np.sum`, `np.mean`, `np.max`, `np.min`, `np.std`, `np.where`. |
| **Pandas** | `read_csv`, `to_csv`, `DataFrame`, `fillna`, `groupby`, `sort_values`, boolean filtering, `value_counts`, `describe`, `concat`. |
| **File Handling** | CSV read/write and text report export (`delivery_report.txt`). |

---

## How to Run

### 1. Install Required Libraries
```bash
py -m pip install numpy pandas matplotlib
```

### 2. Run the Application
```bash
py main.py
```

---

## Author
* **Name:** Yash Kumar Gupta
* **Course:** B.Tech Computer Science & Engineering (Semester 1)
* **Program:** HCL Tech Classroom Training Program
