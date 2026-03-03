
import pandas as pd
from collections import Counter

# ---------- TXT PROCESSING ----------

def process_txt(clean_lines):

    # Remove duplicate lines
    unique_lines = list(set(clean_lines))

    # Word frequency analysis
    words = []
    for line in unique_lines:
        words.extend(line.split())

    word_freq = Counter(words)

    print("\nTop 5 most common words:")
    for word, count in word_freq.most_common(5):
        print(word, ":", count)

    return unique_lines


# ---------- CSV PROCESSING ----------

def process_csv(df):

    # Count missing before
    missing_before = df.isnull().sum().sum()

    # Fill numeric missing
    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].mean())

    # Fill object missing
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Count missing after
    missing_after = df.isnull().sum().sum()
    missing_removed = missing_before - missing_after

    # Now remove duplicates AFTER cleaning
    duplicates_removed = df.duplicated().sum()
    df = df.drop_duplicates()

    print("Duplicates before removing:", duplicates_removed)
    print("Missing values handled:", missing_removed)

    return df, missing_removed, duplicates_removed