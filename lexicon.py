# lexicon.py
from dataset.clean_dataset import clean_text  # Fix the import to correctly use the function

def create_lexicon(df):
    """Creates a lexicon that maps each word to a unique wordID."""
    lexicon = {}
    word_id = 1  # Starting word ID
    
    # Iterate through each document to populate the lexicon
    for index, row in df.iterrows():
        title = row['title']
        words = clean_text(title)  # Use clean_text for cleaning the title text
        
        for word in words:
            if word not in lexicon:
                lexicon[word] = word_id
                word_id += 1  # Increment wordID for each new word
    
    return lexicon
