import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_name = "sales_data.xlsx"
df = pd.read_excel(file_name)

# 📊 Pairplot - Shows relationship between variables
sns.pairplot(df)
plt.show()

# 📉 Scatter Plot - Sales vs TV Ads
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["TV"], y=df["Sales"])
plt.title("TV Advertising vs Sales")
plt.xlabel("TV Advertising Budget ($)")
plt.ylabel("Sales ($)")
plt.show()

# 📊 Heatmap - Correlation Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()
