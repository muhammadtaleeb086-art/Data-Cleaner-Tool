import pandas as pd

# -------- Detect & Handle Outliers --------
def handle_outliers(df):

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    total_outliers = 0
    outlier_indices = set()

    for col in numeric_cols:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]

        count = outliers.shape[0]

        if count > 0:
            print(f"\nColumn: {col}")
            print(f"Outliers detected: {count}")

            total_outliers += count
            outlier_indices.update(outliers.index)

    if total_outliers == 0:
        print("\nNo outliers detected.")
        return df, 0

    print(f"\nTotal Outliers Found: {len(outlier_indices)}")

    choice = input("Do you want to remove outliers? (yes/no): ").lower()

    if choice == "yes":
        df_cleaned = df.drop(index=outlier_indices)
        print("Outliers removed successfully.")
        return df_cleaned, len(outlier_indices)
    else:
        print("Outliers kept in dataset.")
        return df, 0