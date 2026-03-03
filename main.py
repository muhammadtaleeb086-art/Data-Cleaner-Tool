import os
from phase1_input import handle_csv, handle_txt
from phase2_processing import process_txt, process_csv
from phase3_export import export_cleaned_txt, export_cleaned_csv
from phase4_outliers import handle_outliers
from phase5_report import generate_report
from phase5_visualization import visualize_data
from phase6_logging import log_cleaning, view_logs


def main():

    print("\n1. Clean a new dataset")
    print("2. View cleaning history")

    menu_choice = input("Choose an option (1/2): ")

    # ---------- VIEW LOGS ----------
    if menu_choice == "2":
        view_logs()
        return

    elif menu_choice != "1":
        print("Invalid choice.")
        return

    # ---------- CLEANING PIPELINE ----------
    file_path = input("\nEnter file path: ")

    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    # ---------- TXT Pipeline ----------
    if file_path.lower().endswith(".txt"):

        clean_lines = handle_txt(file_path)
        processed_txt = process_txt(clean_lines)
        export_cleaned_txt(processed_txt)

        print("\nTXT File Cleaned & Saved Successfully!")

    # ---------- CSV Pipeline ----------
    elif file_path.lower().endswith(".csv"):

        # Phase 1
        df = handle_csv(file_path)
        original_rows = df.shape[0]

        # Phase 2
        processed_df, missing_removed, duplicates_removed = process_csv(df)

        # Phase 4
        final_df, outliers_removed = handle_outliers(processed_df)
        final_rows = final_df.shape[0]

        # Phase 3
        export_cleaned_csv(final_df)

        # Phase 5 Report
        generate_report(
            original_rows,
            final_rows,
            missing_removed,
            duplicates_removed,
            outliers_removed
        )

        # Phase 5 Visualization (Optional)
        vis_choice = input("\nDo you want to see visualizations? (yes/no): ").lower()

        if vis_choice == "yes":
            visualize_data(final_df)
        else:
            print("Visualization skipped.")

        # Phase 6 Logging
        log_cleaning(
            file_path,
            original_rows,
            final_rows,
            missing_removed,
            duplicates_removed,
            outliers_removed
        )

        print("\nCSV File Cleaned & Saved Successfully!")

    else:
        print("Unsupported file type.")


if __name__ == "__main__":
    main()