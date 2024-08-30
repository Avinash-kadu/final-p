# app/routes.py
from flask import Blueprint, render_template, request
from src.predict import load_model, predict

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        query = request.form['query']
        model, vectorizer = load_model()
        prediction = predict(query, model, vectorizer)
        result = "SQL Injection" if prediction == 1 else "Safe"
    return render_template('index.html', result=result)
