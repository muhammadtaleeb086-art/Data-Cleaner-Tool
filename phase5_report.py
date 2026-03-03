def generate_report(original_rows, final_rows,
                    missing_removed,
                    duplicates_removed,
                    outliers_removed):

    print("\n========== CLEANING REPORT ==========")
    print("Original Rows:", original_rows)
    print("Final Rows:", final_rows)
    print("Missing Values Handled:", missing_removed)
    print("Duplicates Removed:", duplicates_removed)
    print("Outliers Removed:", outliers_removed)

    reduction = original_rows - final_rows
    percent = (reduction / original_rows) * 100

    print("Total Rows Reduced:", reduction)
    print("Data Reduction %:", round(percent, 2), "%")
    print("======================================")