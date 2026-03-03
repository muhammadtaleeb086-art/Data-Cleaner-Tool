import os
import pandas as pd
import textwrap


# -------- Dataset Analysis Function --------
def analyze_dataframe(df):

    print("\n--- Dataset Analysis ---")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")

    print("\n--- Column Data Types ---")
    print(df.dtypes)

    print("\n--- Missing Values ---")
    missing_values = df.isnull().sum()
    print(missing_values)

    print(f"\nDuplicate Rows: {df.duplicated().sum()}")

    return missing_values


# -------- CSV Handling --------
def handle_csv(file_path):

    try:
        df = pd.read_csv(file_path)
        print(f"\nSuccessfully loaded CSV file: {file_path}")

        analyze_dataframe(df)
        return df

    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None


# -------- TXT Cleaning --------
def clean_text(text, line_length=80):

    text = " ".join(text.split())
    text = text.lower()

    sentences = text.split(".")
    cleaned_sentences = []

    for s in sentences:
        s = s.strip()
        if s:
            cleaned_sentences.append(s.capitalize())

    formatted_text = ". ".join(cleaned_sentences)

    if not formatted_text.endswith("."):
        formatted_text += "."

    wrapped_text = textwrap.fill(formatted_text, width=line_length)

    return wrapped_text


# -------- TXT Handling --------
def handle_txt(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned_text = clean_text(raw_text)

    print("\n===== CLEANED TEXT OUTPUT =====\n")
    print(cleaned_text)

    # Dynamic output file name
    base_name = os.path.basename(file_path)
    name = os.path.splitext(base_name)[0]
    output_file = f"output/{name}_cleaned.txt"

    os.makedirs("output", exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(f"\nCleaned TXT saved at: {output_file}")

    lines = cleaned_text.split("\n")
    df = pd.DataFrame(lines, columns=["Cleaned_Text"])

    analyze_dataframe(df)
    return df
    


