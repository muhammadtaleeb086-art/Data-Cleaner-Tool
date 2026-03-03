import sqlite3
from datetime import datetime

def log_cleaning(dataset_name,
                 original_rows,
                 final_rows,
                 missing_removed,
                 duplicates_removed,
                 outliers_removed):

    conn = sqlite3.connect("cleaning_logs.db")
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cleaning_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dataset_name TEXT,
            original_rows INTEGER,
            final_rows INTEGER,
            missing_removed INTEGER,
            duplicates_removed INTEGER,
            outliers_removed INTEGER,
            cleaning_date TEXT
        )
    """)

    cleaning_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO cleaning_logs (
            dataset_name,
            original_rows,
            final_rows,
            missing_removed,
            duplicates_removed,
            outliers_removed,
            cleaning_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        dataset_name,
        original_rows,
        final_rows,
        missing_removed,
        duplicates_removed,
        outliers_removed,
        cleaning_date
    ))

    conn.commit()
    conn.close()

    print("Cleaning log saved to database successfully.")

def view_logs():

    conn = sqlite3.connect("cleaning_logs.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cleaning_logs")
    records = cursor.fetchall()

    if len(records) == 0:
        print("No logs found.")
    else:
        print("\n========== CLEANING HISTORY ==========")
        for row in records:
            print(f"""
ID: {row[0]}
Dataset: {row[1]}
Original Rows: {row[2]}
Final Rows: {row[3]}
Missing Filled: {row[4]}
Duplicates Removed: {row[5]}
Outliers Removed: {row[6]}
Date: {row[7]}
----------------------------------------
""")

    conn.close()