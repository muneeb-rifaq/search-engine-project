import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import re

# Download required NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize NLTK stopwords, lemmatizer, and stemmer
STOPWORDS = set(stopwords.words('english'))  # List of stopwords from NLTK
HELPING_VERBS = {"is", "are", "was", "were", "am", "be", "been", "being", "has", "have", "had", "does", "do", "did", "will", "shall", "should", "can", "could", "may", "might", "must"}
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

def create_lexicon(df):
    lexicon = []
    wordID = 1  # Initialize wordID to 1 (it will be incremented for each unique word)

    # Create a 'docID' column if it doesn't exist
    if 'docID' not in df.columns:
        df['docID'] = df.index  # Use the index as the docID, or another column if applicable

    # Set to store unique words (for eliminating duplicates)
    unique_words = set()

    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        title = row['title']
        
        # Check if the 'title' value is a string and not NaN
        if isinstance(title, str):
            # Clean and split the title into words (removes non-alphabetic characters)
            words = re.findall(r'\b[A-Za-z]+\b', title.lower())  # Only alphabetic words

            for word in words:
                # Apply both stemming and lemmatization
                lemmatized_word = lemmatizer.lemmatize(word)  # Lemmatization
                stemmed_word = stemmer.stem(word)  # Stemming

                # Choose the best representation based on the context:
                final_word = lemmatized_word if lemmatized_word != word else stemmed_word

                # Apply filtering criteria: exclude stop words, helping verbs, and numeric values
                if final_word not in STOPWORDS and final_word not in HELPING_VERBS and final_word.isalpha() and final_word not in unique_words:
                    unique_words.add(final_word)  # Add word to the set of unique words
                    lexicon.append([wordID, final_word])  # Add the word and wordID to the lexicon
                    wordID += 1  # Increment wordID for the next unique word

    return lexicon

# Load the dataset
input_file = r"C:\Users\AT\CSV Dataset files\cleaned_metadata.csv"  # Adjust file path
df = pd.read_csv(input_file)

# Create the lexicon
lexicon = create_lexicon(df)

# Save the lexicon to a new CSV file
output_file = r"lexicon.csv"  # Adjust file path
lexicon_df = pd.DataFrame(lexicon, columns=['wordID', 'word'])
lexicon_df.to_csv(output_file, index=False)
print(f"Lexicon saved to {output_file}")
