from flask import Flask, render_template, request
import pickle

from analysis import preprocess_text
from explainer import explain_sentiment

app = Flask(__name__)

history_data = [
    {"date": "2023-01-01", "text": "Sample query 1", "sentiment": "Positive"},
    {"date": "2023-01-02", "text": "Sample query 2", "sentiment": "Negative"},
]

# Load the pre-trained Logistic Regression model
with open('models/logistic_regression/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the TF-IDF vectorizer used during training
with open('models/logistic_regression/tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    tfidf_vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']

    # Preprocess the user input
    preprocessed_text = preprocess_text(text)

    # Vectorize the preprocessed text
    text_vectorized = tfidf_vectorizer.transform([preprocessed_text])

    sentiment_code = model.predict(text_vectorized)[0]

    if sentiment_code == -1:
        sentiment = 'Negative'
    elif sentiment_code == 1:
        sentiment = 'Positive'
    else:
        sentiment = 'Neutral'

    # explanation = explain_sentiment(text, sentiment)
    # return render_template('index.html', text=text, sentiment=sentiment, explanation=explanation)

    return render_template('index.html', text=text, sentiment=sentiment)


@app.route('/history')
def sentiment_history():
    return render_template('history.html', history=history_data)


if __name__ == '__main__':
    app.run(debug=True)
