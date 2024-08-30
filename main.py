# main.py
from src.data_loader import load_data, preprocess_data, split_data
from src.model import train_model, evaluate_model, save_model


def main():
    # Load data
    queries, labels = load_data('data/sql_injections.csv')

    # Preprocess data
    X, vectorizer = preprocess_data(queries)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(X, labels)

    # Train model
    model = train_model(X_train, y_train)

    # Evaluate model
    evaluate_model(model, X_test, y_test)

    # Save model and vectorizer
    save_model(model, vectorizer)


if __name__ == "__main__":
    main()
