import pandas as pd # 
import os
from dataset.load_dataset import process_and_save_in_chunks
from dataset.clean_dataset import clean
from lexicon import create_lexicon
from forward_indexing import create_forward_index
from inverted_indexing import create_inverted_index
#import nltk
#import re  # Import regex for text cleaning
#from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
#from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
#nltk.download('punkt')
#nltk.download('punkt_tab')
#nltk.download('stopwords')
#nltk.download('wordnet')


chunk_size = 10000  # alows user to chnge chunk size based on differences in comp specs
max_rows = 60000 # max rows of articles that will be processed

# explain all the files used where all the initial , intermediate and final files are stored

dataset_path = r"C:\Users\hp\Downloads\medium_articles\medium_articles.csv"# location in downloads with articles file

processed_dataset_path = r"C:\Users\hp\Documents\GitHub\search-engine-project\processed_dataset.csv"# location where processed dataset is stored

input_file = r"C:\Users\hp\Documents\GitHub\search-engine-project\cleaned_dataset.csv"  # location of cleaned dataset which is used to make different INDEX
lexicon_output_file = r"lexicon.csv"# file containing lexicon
forward_index_output_file = r"forward_index.csv" # file containing forward index
inverted_index_output_file = r"inverted_index.csv"# file containing inverted index


def append_to_csv(file_path, data, mode='w'):
    if os.path.exists(file_path):
        mode = 'a'  # Appends if file exists
    else:
        mode = 'w'  # creates a file if does not exist
    pd.DataFrame(data).to_csv(file_path, mode=mode, header=(mode=='w'), index=False)

#  lexicon, forward index, and inverted index initilizations
lexicon = {}
forward_index = {}
inverted_index = {}

# Function to process each chunk and update lexicon, forward index, and inverted index
def process_chunk(chunk):
    global lexicon, forward_index, inverted_index

    # Step 1: Add to or Create or update lexicon
    #print("Adding to Lexicon")
    lexicon = create_lexicon(chunk, lexicon)#Hello this is a change
    
    # Step 2: Add to or Create forward index using the lexicon
    #print("Adding to Forward Index")
    forward_index_chunk = create_forward_index(chunk, lexicon)
    
    # Step 3: Add to or Create inverted index using the forward index
    #print("Adding to Inverted Index")
    inverted_index_chunk = create_inverted_index(forward_index_chunk)
    
    forward_index_data = [{'docID': docID, 'wordIDs': word_ids} for docID, word_ids in forward_index_chunk.items()]
    inverted_index_data = [{'wordID': word_id, 'docIDs': doc_ids} for word_id, doc_ids in inverted_index_chunk.items()]

    append_to_csv(lexicon_output_file, [{'word': word, 'wordID': word_id} for word, word_id in lexicon.items()])
    append_to_csv(forward_index_output_file, forward_index_data)
    append_to_csv(inverted_index_output_file, inverted_index_data)

#  process content of dataset in chunks

print('Reading Original file and making processed file ')
process_and_save_in_chunks(dataset_path, processed_dataset_path, max_rows)


print('Reading processed file and making Cleaned file ')
clean(processed_dataset_path, input_file)

print('Chunk Processing ')
for chunk in pd.read_csv(input_file, chunksize=chunk_size, encoding='utf-8', on_bad_lines='skip'):
    print(f"Processing chunk with {len(chunk)} rows...")
    
    # Process the chunk
    process_chunk(chunk)

print("Processing complete!")



# I hope this implementation of the search engine has proved succesful
# On behalf of me and my Teammates, I thank you for reading it

