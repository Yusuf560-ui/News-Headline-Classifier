import joblib
import time

model = joblib.load('final_model.joblib')
print("Model loaded successfully.")


vectoriser = joblib.load('vectoriser.joblib')
print("Vectorizer loaded successfully.")
print("All components loaded successfully.")
print("\n")

# Now you can use `model` and `vectoriser` as needed

# Example usage:


def predict_headline(headline):
    X = vectoriser.transform([headline])
    prediction = model.predict(X)
    return prediction[0]

for x in range(1,6):
    headline = input("Enter an headline to classify: ").lower().strip()
    category = predict_headline(headline)
    time.sleep(1)

    print("\n")
    print("------------")
    print(f"Headline Categoty: {category.upper()}")
    print("------------")
    print("\n")