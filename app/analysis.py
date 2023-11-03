import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

nltk.download('stopwords')
nltk.download('punkt')

# Define a function for text preprocessing
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Perform text normalization (lowercasing and removing special characters)
    normalized_tokens = [re.sub(r'[^a-zA-Z0-9]', '', word).lower() for word in filtered_tokens]
    
    # Remove empty tokens
    normalized_tokens = [token for token in normalized_tokens if token != '']

    # Join the tokens back into a string
    preprocessed_text = ' '.join(normalized_tokens)
    
    return preprocessed_text