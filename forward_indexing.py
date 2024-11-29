# create_forward_index.py

from lexicon import lexicon
from clean_dataset import clean_dataset

def create_forward_index(df):
    """Creates the forward index using the provided lexicon."""
    forward_index = {}
    
    # Iterate through each document to create the forward index
    for index, row in df.iterrows():
        title = row['title']
        words = clean_dataset(title)
        
        word_ids_for_doc = [lexicon[word] for word in words if word in lexicon]
        forward_index[index] = word_ids_for_doc  # Store word IDs for the document
    
    return forward_index
