import pandas as pd
import os

def clean_metadata(input_file, output_file):
    # Step 1: Check if the file exists
    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        return
    
    # Load the dataset
    df = pd.read_csv(input_file, encoding='utf-8', on_bad_lines='skip')

    # Step 2: Inspect the data (Optional - can be removed in production)
    print("First 5 rows of the dataset:")
    print(df.head())

    print("\nColumn names and data types:")
    print(df.dtypes)

    # Step 3: Remove duplicate rows (if any)
    df = df.drop_duplicates()

    # Step 4: Handle missing values
    # Option 1: Remove rows with missing values in certain columns
    if 'column_name1' in df.columns:
        df = df.dropna(subset=['column_name1', 'column_name2'])  # Specify relevant columns
    else:
        print("Columns 'column_name1' or 'column_name2' not found in the dataset.")

    # Step 5: Fix data types if necessary
    if 'date_column' in df.columns:
        df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')  # Convert date columns
    else:
        print("Column 'date_column' not found in the dataset.")

    if 'numeric_column' in df.columns:
        df['numeric_column'] = pd.to_numeric(df['numeric_column'], errors='coerce')  # Convert numeric columns
    else:
        print("Column 'numeric_column' not found in the dataset.")

    # Step 6: Drop irrelevant columns
    irrelevant_columns = ['irrelevant_column1', 'irrelevant_column2']
    for col in irrelevant_columns:
        if col in df.columns:
            df = df.drop(columns=[col])
        else:
            print(f"Column '{col}' not found in the dataset.")

    # Step 7: Normalize text
    if 'title_column' in df.columns:
        df['title_column'] = df['title_column'].str.strip().str.lower()
    else:
        print("Column 'title_column' not found in the dataset.")

    # Step 8: Save the cleaned data to a new file
    df.to_csv(output_file, index=False)

    print(f"Data cleaning complete. Cleaned file saved to: {output_file}")

# Specify the correct file paths
input_path = r"C:\Users\AT\Downloads\medium_articles.csv\medium_articles.csv"  # Update with correct file path
output_path = r"C:\Users\AT\Documents\GitHub\search-engine-project\cleaned_metadata.csv"

clean_metadata(input_path, output_path)
