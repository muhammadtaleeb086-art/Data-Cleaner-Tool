import os
import pandas as pd

# -------- Create Output Folder --------
def create_output_folder():
    if not os.path.exists("output"):
        os.makedirs("output")

# -------- Export Final Cleaned TXT --------
def export_cleaned_txt(cleaned_text):

    create_output_folder()

    output_path = os.path.join("output", "final_cleaned.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        for line in cleaned_text:
            f.write(line + "\n")

    print("Final Cleaned TXT saved at:", output_path)


# -------- Export Final Cleaned CSV --------
def export_cleaned_csv(df):

    create_output_folder()

    output_path = os.path.join("output", "final_cleaned.csv")

    df.to_csv(output_path, index=False)

    print("Final Cleaned CSV saved at:", output_path)


# -------- Export Summary Report --------
def export_summary_report(original_rows, cleaned_rows, missing_removed, duplicates_removed):

    create_output_folder()

    report_path = os.path.join("output", "summary_report.txt")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("----- DATA CLEANING SUMMARY -----\n")
        f.write(f"Original Rows: {original_rows}\n")
        f.write(f"Cleaned Rows: {cleaned_rows}\n")
        f.write(f"Missing Values Removed: {missing_removed}\n")
        f.write(f"Duplicate Rows Removed: {duplicates_removed}\n")

    print("Summary Report saved at:", report_path)