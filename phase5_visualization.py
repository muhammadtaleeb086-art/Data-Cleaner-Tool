import matplotlib.pyplot as plt

def visualize_data(df):

    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) == 0:
        print("No numeric columns available for visualization.")
        return

    # -------- Histograms --------
    for col in numeric_cols:
        plt.figure()
        df[col].hist()
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.show()

    # -------- Boxplot --------
    plt.figure()
    df[numeric_cols].boxplot()
    plt.title("Boxplot of Numeric Columns")
    plt.xticks(rotation=45)
    plt.show()