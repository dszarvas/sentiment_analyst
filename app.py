from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

from analysis import preprocess_text
from util import load_models
from database.database import db, insert_history, History

app = Flask(__name__, )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///history.db'
db.init_app(app)

model, tfidf_vectorizer = load_models()

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

    insert_history(date=datetime.now().date(), text=text, sentiment=sentiment)

    return render_template('index.html', text=text, sentiment=sentiment)

@app.route('/history')
def sentiment_history():
    history_data = History.query.all()
    return render_template('history.html', history=history_data)

@app.route('/clear_database', methods=['POST'])
def clear_database():
    # Delete all records in the History table
    History.query.delete()
    db.session.commit()
    return redirect(url_for('sentiment_history'))  # Redirect to the history page

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
