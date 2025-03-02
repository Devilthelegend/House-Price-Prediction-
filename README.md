House Price Prediction using Flask

📌 Project Overview

This is a House Price Prediction Web App built using Flask, Scikit-learn, and Pandas. Users can input the number of bedrooms, bathrooms, square footage, and location to get an estimated house price.

🚀 Features

User-friendly Web Interface for inputting house details

Machine Learning Model (Linear Regression) for price prediction

One-Hot Encoding for categorical location input

Error Handling for missing or incorrect data

Deployed Locally using Flask

🏗️ Tech Stack

Backend: Flask (Python)

Machine Learning: Scikit-learn, Pandas, NumPy

Frontend: HTML, CSS

Model Deployment: Joblib for saving/loading the model

📂 Project Structure

/house-price-prediction
│-- static/             # Static files (CSS, JS, Images)
│-- templates/          # HTML templates
│   │-- index.html      # Home page
│   │-- predict.html    # Result page
│-- model.pkl          # Trained ML model
│-- features.pkl       # Feature list used in the model
│-- house_prices.csv   # Dataset (if needed)
│-- app.py             # Flask app
│-- model.py           # ML Model training script
│-- README.md          # Project Documentation

⚙️ Installation & Setup

🔹 Step 1: Clone the Repository

git clone (https://github.com/Devilthelegend/House-Price-Prediction-.git)
cd house-price-prediction

🔹 Step 2: Create a Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

pip install -r requirements.txt

🔹 Step 3: Train the Model

Ensure house_prices.csv is in the directory and run:

python model.py

This will train the model and save model.pkl and features.pkl.

🔹 Step 4: Run the Flask App

python app.py

The app will run at http://127.0.0.1:5000.

🖥️ Usage Guide

Open http://127.0.0.1:5000 in your browser.

Enter bedrooms, bathrooms, square footage, and location.

Click "Predict Price".

The predicted house price will be displayed.

🔥 Example Prediction

Bedrooms : 3

Bathrooms:2

Sqft:1500

Location:Location1

Predicted Price:₹12,50,000

🛠️ Troubleshooting

🔴 FileNotFoundError: model.pkl Not Found

✅ Solution: Run python model.py to train the model.

🔴 KeyError: 'sqft' not in index

✅ Solution: Check house_prices.csv column names. If sqft is missing, rename area to sqft in model.py.

🔴 Method Not Allowed (405 Error)

✅ Solution: Ensure <form> in index.html has method="POST".

🤝 Contributing

Pull requests are welcome! Open an issue for major changes.

📜 License

This project is licensed under the MIT License.

📞 Contact

For queries, reach out via GitHub Issues
