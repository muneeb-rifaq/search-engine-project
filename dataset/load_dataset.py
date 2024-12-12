import os
import pandas as pd # 

def process_and_save_in_chunks(input_file, output_file, chunk_size, max_rows): 
    """Process up to max_rows of the dataset in chunks and save to a new CSV."""
    chunk_count = 0
    total_rows_processed = 0  # Count number of rows processed

    # Clear the output file before writing new data
    if os.path.exists(output_file):
        os.remove(output_file)

    for chunk in pd.read_csv(input_file, chunksize=chunk_size, encoding='utf-8', on_bad_lines='skip'):
        if total_rows_processed >= max_rows:
            break  # Ensure rows <  max_rows limit
        
        chunk_count += 1
        print(f"Processing chunk {chunk_count}")

        # Calculate how many rows to write from this chunk
        rows_to_process = min(max_rows - total_rows_processed, len(chunk))
        if rows_to_process <= 0:
            break
        
        # Truncate the chunk to the rows that fit within the limit
        truncated_chunk = chunk.head(rows_to_process)

        # Append the truncated chunk to the output file
        truncated_chunk.to_csv(output_file, mode='a', header=(chunk_count == 1), index=False)

        # Update the total rows processed
        total_rows_processed += rows_to_process

    print(f"Data processing complete. Processed {total_rows_processed} rows across {chunk_count} chunks.")