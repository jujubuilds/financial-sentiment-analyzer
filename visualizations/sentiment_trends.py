import pandas as pd
import plotly.express as px

def plot_sentiment_trends(data_file):
    """Plot sentiment trends over time."""
    df = pd.read_csv(data_file)
    df['date'] = pd.to_datetime(df['date'])
    sentiment_counts = df.groupby([df['date'].dt.date, 'sentiment']).size().reset_index(name='counts')
    fig = px.line(sentiment_counts, x='date', y='counts', color='sentiment', title='Sentiment Trends')
    fig.show()

if __name__ == '__main__':
    plot_sentiment_trends('../data/processed_data.csv')
