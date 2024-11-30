import pandas as pd
import os
from lexicon import create_lexicon
from forward_indexing import create_forward_index
from inverted_indexing import create_inverted_index

# Define the chunk size for batch processing
chunk_size = 10000  # Adjust chunk size depending on your system's memory capacity

# Define the input and output files
input_file = r"C:\Users\AT\Documents\GitHub\search-engine-project\cleaned_dataset.csv"  # Adjust path to your cleaned dataset
lexicon_output_file = r"lexicon.csv"
forward_index_output_file = r"forward_index.csv"
inverted_index_output_file = r"inverted_index.csv"

# Function to append results to CSV (avoiding overwriting)
def append_to_csv(file_path, data, mode='w'):
    if os.path.exists(file_path):
        mode = 'a'  # Append mode if file exists
    else:
        mode = 'w'  # Write mode if file does not exist
    pd.DataFrame(data).to_csv(file_path, mode=mode, header=(mode=='w'), index=False)

# Initialize the lexicon, forward index, and inverted index
lexicon = {}
forward_index = {}
inverted_index = {}

# Function to process each chunk and update lexicon, forward index, and inverted index
def process_chunk(chunk):
    global lexicon, forward_index, inverted_index
    
    # Step 1: Create or update lexicon
    lexicon = create_lexicon(chunk, lexicon)

    # Step 2: Create forward index using the lexicon
    forward_index_chunk = create_forward_index(chunk, lexicon)
    
    # Step 3: Create inverted index using the forward index
    inverted_index_chunk = create_inverted_index(forward_index_chunk)
    
    # Step 4: Save the chunk results to respective CSV files
    forward_index_data = [{'docID': docID, 'wordIDs': word_ids} for docID, word_ids in forward_index_chunk.items()]
    inverted_index_data = [{'wordID': word_id, 'docIDs': doc_ids} for word_id, doc_ids in inverted_index_chunk.items()]

    append_to_csv(lexicon_output_file, [{'word': word, 'wordID': word_id} for word, word_id in lexicon.items()])
    append_to_csv(forward_index_output_file, forward_index_data)
    append_to_csv(inverted_index_output_file, inverted_index_data)

# Load and process the dataset in chunks
for chunk in pd.read_csv(input_file, chunksize=chunk_size, encoding='utf-8', on_bad_lines='skip'):
    print(f"Processing chunk with {len(chunk)} rows...")
    
    # Process the chunk
    process_chunk(chunk)

print("Processing complete!")
