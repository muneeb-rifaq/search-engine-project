# clean_text.py

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text):
    """Cleans and processes the text (tokenization, stopword removal, and lemmatization)."""
    if isinstance(text, str):
        text = text.lower()
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token.isalpha()]  # Remove non-alphabetic tokens
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]  # Remove stopwords
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]  # Lemmatize tokens
        return tokens
    return []  # Return empty list for non-string values
