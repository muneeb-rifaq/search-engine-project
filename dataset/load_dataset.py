import pandas as pd

def process_and_save_in_chunks(input_file, output_file, chunk_size=10000):
    """Process the dataset in chunks and save to a new CSV."""
    chunk_count = 0
    for chunk in pd.read_csv(input_file, chunksize=chunk_size, encoding='utf-8', on_bad_lines='skip'):
        chunk_count += 1
        print(f"Processing chunk {chunk_count}")
        # Example: You can process the chunk here (e.g., clean, transform, etc.)
        
        # Append the chunk to a new CSV file
        chunk.to_csv(output_file, mode='a', header=(chunk_count == 1), index=False)
        
    print(f"Data processing complete. {chunk_count} chunks processed.")

# Path to your dataset
dataset_path = r"C:\Users\AT\Downloads\medium_articles.csv\medium_articles.csv"  # Update with your dataset path
output_path = r"C:\Users\AT\Documents\GitHub\search-engine-project\processed_dataset.csv"  # Path where processed data will be saved

process_and_save_in_chunks(dataset_path, output_path)
