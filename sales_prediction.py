import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the dataset
file_name = "sales_data.xlsx"
df = pd.read_excel(file_name)

# Features (X) and Target (y)
X = df[["TV", "Radio", "Newspaper"]]  # Independent Variables
y = df["Sales"]  # Dependent Variable

# Split data into training & testing sets (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression Model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Print Model Performance
print("📊 Model Performance:")
print(f"MAE  (Mean Absolute Error): {mae:.2f}")
print(f"MSE  (Mean Squared Error): {mse:.2f}")
print(f"RMSE (Root Mean Squared Error): {rmse:.2f}")
print(f"R² Score: {r2:.2f}")

# Scatter Plot: Actual vs Predicted Sales
plt
import joblib

# Save the trained model
model_filename = "sales_model.pkl"
joblib.dump(model, model_filename)

print(f"✅ Model saved as '{model_filename}'")

