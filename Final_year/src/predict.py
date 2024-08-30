# src/predict.py
import joblib

def load_model(model_path='models/sql_injection_model.pkl', vectorizer_path='models/vectorizer.pkl'):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer

def predict(query, model, vectorizer):
    X = vectorizer.transform([query])
    prediction = model.predict(X)
    return prediction[0]
