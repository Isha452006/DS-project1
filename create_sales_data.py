import pandas as pd

# Sample sales data
data = {
    "TV": [230.1, 44.5, 17.2, 151.5, 180.8, 8.7, 57.5, 120.2, 8.6, 199.8],
    "Radio": [37.8, 39.3, 45.9, 41.3, 10.8, 48.9, 32.8, 19.6, 2.1, 2.6],
    "Newspaper": [69.2, 45.1, 69.3, 58.5, 58.4, 75, 23.5, 11.6, 1, 21.2],
    "Sales": [22.1, 10.4, 9.3, 18.5, 12.9, 7.2, 11.8, 13.2, 4.8, 10.6]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save the file
file_name = "sales_data.xlsx"
df.to_excel(file_name, index=False)

print(f"✅ '{file_name}' has been created successfully!")
