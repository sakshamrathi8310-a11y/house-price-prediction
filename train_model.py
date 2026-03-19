import pandas as pd
import pickle as pk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv(r"C:\\projects\\house_price_prediction\\cleaned_data_csv")

# Remove useless column
data = data.drop(columns=["Unnamed: 0"])

# One-hot encoding for location
data = pd.get_dummies(data, columns=["location"])

# Features and target
X = data.drop("price", axis=1)
y = data["price"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
score = model.score(X_test, y_test)
print("Model Accuracy:", score)

# Save model
pk.dump(model, open("House_price_prediction_model.pkl", "wb"))

print("Model saved successfully!")