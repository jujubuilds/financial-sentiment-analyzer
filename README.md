# Financial Sentiment Analyzer

## Overview
This project analyzes financial news articles and predicts their sentiment (positive, neutral, or negative) using machine learning.

### Features
1. **Fetch Financial News**: Pull articles using NewsAPI.
2. **Preprocess Data**: Clean and tokenize text for analysis.
3. **Train Sentiment Model**: Use Naive Bayes for classification.
4. **Visualize Sentiment Trends**: Analyze sentiment trends over time with Plotly.

### Tech Stack
- **Python**: Pandas, scikit-learn, NLTK, Plotly
- **APIs**: NewsAPI for data fetching

### Setup
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd financial-sentiment-analyzer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the pipeline:
   - Fetch news: `python src/fetch_news.py`
   - Preprocess data: `python src/preprocess.py`
   - Train model: `python src/train_model.py`
   - Visualize trends: `python visualizations/sentiment_trends.py`

### Future Enhancements
- Use a pre-trained model like FinBERT for more accurate sentiment analysis.
- Add more advanced visualizations.
- Extend support to multiple news sources.
