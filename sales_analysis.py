import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv(r"C:\Users\leela\OneDrive\Desktop\Sales_Revenue_Dashboard\data\sales.csv")

# Show first rows
print(df.head())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna(0, inplace=True)

# Total Sales
total_sales = df['Sales'].sum()

print("Total Sales:", total_sales)

# Sales Graph
monthly_sales = df.groupby('Category')['Sales'].sum()

monthly_sales.plot(kind='bar')

plt.title("Category Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()

# Save cleaned data
df.to_csv(r"C:\Users\leela\OneDrive\Desktop\Sales_Revenue_Dashboard\outputs\cleaned_sales.csv", index=False)

print("Project completed successfully!")