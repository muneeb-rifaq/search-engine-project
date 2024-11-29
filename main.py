# main.py
import pandas as pd
from lexicon import create_lexicon  # Import create_lexicon function correctly
from forward_indexing import create_forward_index  # Import the correct forward index function
from inverted_indexing import create_inverted_index  # Import the correct inverted index function

# Load your dataset
input_file = r"C:\Users\AT\CSV Dataset files\cleaned_metadata.csv"  # Adjust file path
df = pd.read_csv(input_file)

# 1. Create the lexicon
lexicon = create_lexicon(df)  # Pass df to create_lexicon

# 2. Create the forward index using the lexicon
forward_index = create_forward_index(df, lexicon)  # Pass both df and lexicon

# 3. Create the inverted index from the forward index
inverted_index = create_inverted_index(forward_index)

# Export lexicon to CSV
lexicon_data = [{'word': word, 'wordID': word_id} for word, word_id in lexicon.items()]
lexicon_df = pd.DataFrame(lexicon_data)
lexicon_output_file = r"lexicon.csv"
lexicon_df.to_csv(lexicon_output_file, index=False)
print(f"Lexicon saved to {lexicon_output_file}")

# Export forward index to CSV
forward_index_data = []
for docID, word_ids in forward_index.items():
    forward_index_data.append({'docID': docID, 'wordIDs': word_ids})

forward_index_df = pd.DataFrame(forward_index_data)
forward_index_output_file = r"forward_index.csv"
forward_index_df.to_csv(forward_index_output_file, index=False)
print(f"Forward index saved to {forward_index_output_file}")

# Export inverted index to CSV
inverted_index_data = []
for word_id, doc_ids in inverted_index.items():
    inverted_index_data.append({'wordID': word_id, 'docIDs': doc_ids})

inverted_index_df = pd.DataFrame(inverted_index_data)
inverted_index_output_file = r"inverted_index.csv"
inverted_index_df.to_csv(inverted_index_output_file, index=False)
print(f"Inverted index saved to {inverted_index_output_file}")
