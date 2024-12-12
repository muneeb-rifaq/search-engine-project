import pandas as pd # 
import nltk
import re  # Import regex for text cleaning
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def clean_text(text):
    """Cleans and processes the text (tokenization, stopword removal, and lemmatization)."""
    if isinstance(text, str):
        text = text.lower()
        #  remove any non-alphabetic characters (eg '@123', '1983', ":@dsgf")
        text = re.sub(r'[^a-zA-Z\s]', '', text)  # Removes non-alphabet characters
        
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        
        # delete stopwords 
        tokens = [token for token in tokens if token not in stop_words and token.isalpha()]
        
        lemmatizer = WordNetLemmatizer()
        
        # Lemmatize  (e.g., jump, jumping, jumped to 'jump')
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return tokens
    return []  # Return empty list for non-string values (like NaN)

def clean(input_file, output_file):
    """Cleans the dataset by applying the clean_text function to the 'title' column and saves it to a new file."""
    
    df = pd.read_csv(input_file)

    # Make sure the 'title' column is present in the file
    if 'title' in df.columns:
        # call the clean_text function to the column
        df['cleaned_title'] = df['title'].apply(clean_text)
    else:
        print("Error: 'title' column not found in the dataset.")
        return

    # Save the cleaned dataset to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Cleaned dataset saved to {output_file}")