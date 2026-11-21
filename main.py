import data_handler
import analytics_engine


def print_banner():
    print("\n" + "=" * 58)
    print("     FOOD DELIVERY & RESTAURANT SALES ANALYSER (v1.0)")
    print("     Built with Python, NumPy, Pandas & Matplotlib")
    print("=" * 58)


def print_menu():
    print("-------------------- MAIN MENU --------------------")
    print("  1. Display All Orders (60+ Records)")
    print("  2. Add New Order")
    print("  3. Search Order (by ID, Customer, or City)")
    print("  4. Update Existing Order")
    print("  5. Delete Order")
    print("  6. NumPy Statistical Analysis (1D/2D & Slicing)")
    print("  7. Pandas GroupBy Insights (City / Category / Pay)")
    print("  8. Filter & Sort Orders (Top 10 / Late / City)")
    print("  9. Generate & Export Summary Report (.txt)")
    print(" 10. Show Visual Sales Dashboard (2 Graphs)")
    print(" 11. Exit")
    print("---------------------------------------------------")


def run_app():
    # Step 1: Ensure 60-record CSV dataset exists
    data_handler.create_dataset()
    print_banner()

    # Step 2: Interactive Menu Loop
    while True:
        print_menu()
        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":
            data_handler.display_all_orders()
        elif choice == "2":
            data_handler.add_order()
        elif choice == "3":
            data_handler.search_order()
        elif choice == "4":
            data_handler.update_order()
        elif choice == "5":
            data_handler.delete_order()
        elif choice == "6":
            analytics_engine.numpy_statistical_analysis()
        elif choice == "7":
            analytics_engine.pandas_groupby_analysis()
        elif choice == "8":
            analytics_engine.filter_and_sort_orders()
        elif choice == "9":
            analytics_engine.generate_summary_report()
        elif choice == "10":
            analytics_engine.show_visual_dashboard()
        elif choice == "11":
            print("\nExiting Food Delivery Analyser. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 11.\n")


if __name__ == "__main__":
    try:
        run_app()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting safely.")