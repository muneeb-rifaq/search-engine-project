import pandas as pd
import nltk
import re  # Import regex for text cleaning
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Define the text cleaning function
def clean_text(text):
    """Cleans and processes the text (tokenization, stopword removal, and lemmatization)."""
    if isinstance(text, str):
        text = text.lower()
        # Use regex to remove any non-alphabetic characters (i.e., punctuation, numbers)
        text = re.sub(r'[^a-zA-Z\s]', '', text)  # Removes non-alphabet characters
        
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        
        # Remove stopwords from the tokenized text
        tokens = [token for token in tokens if token not in stop_words and token.isalpha()]
        
        lemmatizer = WordNetLemmatizer()
        
        # Lemmatize tokens (e.g., 'running' -> 'run')
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return tokens
    return []  # Return empty list for non-string values

# Load the processed dataset (replace with the actual path to your processed dataset)
input_file = r"C:\Users\AT\Documents\GitHub\search-engine-project\processed_dataset.csv"  # Specify the correct path to your file
df = pd.read_csv(input_file)

# Ensure the 'title' column exists (or adjust to another column if needed)
if 'title' in df.columns:
    # Apply the clean_text function to the 'title' column
    df['cleaned_title'] = df['title'].apply(clean_text)
else:
    print("Error: 'title' column not found in the dataset.")
    exit()

# Save the cleaned dataset to a new CSV file
output_file = r"C:\Users\AT\Documents\GitHub\search-engine-project\cleaned_dataset.csv"  # Specify the path where you want to save the cleaned dataset
df.to_csv(output_file, index=False)

print(f"Cleaned dataset saved to {output_file}")
