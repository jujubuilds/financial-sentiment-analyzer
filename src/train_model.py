import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pickle

def train_model(data_file, model_file):
    """Train a sentiment analysis model."""
    df = pd.read_csv(data_file)
    df['sentiment'] = [1 if 'profit' in text.lower() else 0 for text in df['cleaned_content']]
    
    X = df['cleaned_content']
    y = df['sentiment']
    
    vectorizer = TfidfVectorizer()
    X_vectors = vectorizer.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_vectors, y, test_size=0.2, random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    
    with open(model_file, 'wb') as f:
        pickle.dump((model, vectorizer), f)

if __name__ == '__main__':
    train_model('../data/processed_data.csv', '../models/sentiment_model.pkl')
