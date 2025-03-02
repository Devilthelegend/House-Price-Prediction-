import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib
import os

# Load dataset
df = pd.read_csv("house_prices.csv")

# Drop missing values
df = df.dropna()

# Check and rename area column if needed
if "sqft" not in df.columns:
    if "area" in df.columns:
        print("Column 'sqft' not found, using 'area' instead.")
        df.rename(columns={"area": "sqft"}, inplace=True)
    else:
        raise KeyError("Neither 'sqft' nor 'area' found in the dataset.")

# Define features and target variable
features = ["bedrooms", "bathrooms", "sqft"]
if "location" in df.columns:
    features.append("location")

target = "price"

# One-hot encode categorical features
if "location" in df.columns:
    df = pd.get_dummies(df, columns=["location"], drop_first=True)

# Separate features and target variable
X = df[features]
y = df[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Align train and test data to ensure they have the same features
X_train, X_test = X_train.align(X_test, join="left", axis=1, fill_value=0)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred):.2f}")

# Save model and feature names
joblib.dump(model, "model.pkl")
joblib.dump(X_train.columns.tolist(), "features.pkl")

# Confirm files are saved
if os.path.exists("model.pkl") and os.path.exists("features.pkl"):
    print("✅ Model and feature names saved successfully!")
else:
    print("❌ Error: Model or feature names were not saved correctly!")
