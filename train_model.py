import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data (Make sure 'sales_data.xlsx' is in the same folder)
df = pd.read_excel("sales_data.xlsx")

# Define features and target variable
X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, " sales_model.pkl")

print("✅ Model saved as 'sales_model.pkl'")
