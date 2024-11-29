# forward_indexing.py
from lexicon import create_lexicon  # Correct the import for create_lexicon
from dataset.clean_dataset import clean_text  # Fix the import for clean_text

def create_forward_index(df, lexicon):
    """Creates the forward index using the provided lexicon."""
    forward_index = {}
    
    # Iterate through each document to create the forward index
    for index, row in df.iterrows():
        title = row['title']
        words = clean_text(title)  # Use clean_text for cleaning the title text
        
        word_ids_for_doc = [lexicon[word] for word in words if word in lexicon]
        forward_index[index] = word_ids_for_doc  # Store word IDs for the document
    
    return forward_index
