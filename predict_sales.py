import joblib
import numpy as np

# Load the saved model
model_filename = "sales_model.pkl"
model = joblib.load(model_filename)

# Example input (TV, Radio, Newspaper)
new_data = np.array([[200, 30, 20]])  # Modify these values

# Predict sales
predicted_sales = model.predict(new_data)

print(f"📢 Predicted Sales: {predicted_sales[0]:.2f}")
