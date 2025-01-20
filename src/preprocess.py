import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    """Clean and preprocess text data."""
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_words)

def preprocess_data(input_file, output_file):
    """Preprocess raw article data."""
    df = pd.read_csv(input_file)
    df['cleaned_content'] = df['content'].apply(preprocess_text)
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    preprocess_data('../data/raw_articles.csv', '../data/processed_data.csv')
