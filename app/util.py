import pickle

def load_models():
    # Load the pre-trained Logistic Regression model
    with open('models/logistic_regression/model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    # Load the TF-IDF vectorizer used during training
    with open('models/logistic_regression/tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
        tfidf_vectorizer = pickle.load(vectorizer_file)

    return model, tfidf_vectorizer