import pandas as pd
import os

# Check current working directory
print("📂 Current Directory:", os.getcwd())

# File path
file_name = "sales_data.xlsx"

# Check if file exists before loading
if os.path.exists(file_name):
    df = pd.read_excel(file_name)
    print("✅ File loaded successfully!")
    print(df.head())  # Show first 5 rows
else:
    print("❌ ERROR: File not found. Check the directory.")
