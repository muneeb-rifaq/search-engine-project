import pandas as pd
import re
from dataset.clean_dataset import clean_text  # Assuming you're using clean_text for tokenization and cleaning

def create_lexicon(df, lexicon):
    """Creates a lexicon that maps each word to a unique wordID."""
    word_id = len(lexicon) + 1  # Start from the next available wordID
    
    # Iterate through each document to populate the lexicon
    for index, row in df.iterrows():
        title = row['title']  # Assuming the 'title' column contains cleaned titles
        
        # Clean and tokenize the title using the clean_text function
        words = clean_text(title)
        
        # Add words to lexicon and assign unique word ID
        for word in words:
            if word not in lexicon:
                lexicon[word] = word_id
                word_id += 1  # Increment wordID for each new word
    
    return lexicon

# Function to process the dataset in chunks
def process_chunks(input_file, chunk_size=10000):
    """Process the dataset in chunks and update the lexicon."""
    lexicon = {}  # Initialize lexicon
    
    # Read the input file in chunks
    for chunk in pd.read_csv(input_file, chunksize=chunk_size, encoding='utf-8', on_bad_lines='skip'):
        print(f"Processing chunk with {len(chunk)} rows...")
        # Update the lexicon for the current chunk
        lexicon = create_lexicon(chunk, lexicon)
    
    return lexicon

# Example usage
input_file = r"C:\Users\AT\Documents\GitHub\search-engine-project\cleaned_dataset.csv"  # Adjust to the correct path
lexicon = process_chunks(input_file)

# Print the lexicon
print(lexicon)
