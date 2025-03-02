from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load trained model and feature list
if os.path.exists("model.pkl") and os.path.exists("features.pkl"):
    model = joblib.load("model.pkl")
    features = joblib.load("features.pkl")
else:
    raise FileNotFoundError("❌ Error: Model file or features file not found!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        user_input = {
            "bedrooms": float(request.form["bedrooms"]),
            "bathrooms": float(request.form["bathrooms"]),
            "sqft": float(request.form["sqft"])
        }

        # Handle location input (if present)
        if "location" in request.form:
            location = "location_" + request.form["location"]
            user_input[location] = 1  # One-hot encoding for location

        # Convert input to DataFrame
        input_df = pd.DataFrame([user_input])

        # Align input data with trained features
        input_df = input_df.reindex(columns=features, fill_value=0)  # Fill missing columns with 0

        # Predict price
        prediction = model.predict(input_df)[0]

        return render_template("predict.html", prediction=round(prediction, 2))

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
