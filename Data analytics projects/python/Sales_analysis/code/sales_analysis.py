# ===============================
# SALES PERFORMANCE ANALYSIS
# ===============================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("dataset.csv")

# Preview Data
print("First 5 Rows")
print(df.head())

# -------------------------------
# Dataset Information
# -------------------------------
print("\nDataset Info")
print(df.info())

# -------------------------------
# Check Missing Values
# -------------------------------
print("\nMissing Values")
print(df.isnull().sum())

# -------------------------------
# Basic Business Metrics
# -------------------------------
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_quantity = df['Quantity'].sum()

print("\n===== BUSINESS SUMMARY =====")
print(f"Total Sales: {total_sales}")
print(f"Total Profit: {total_profit}")
print(f"Total Quantity Sold: {total_quantity}")

# -------------------------------
# Sales by Region
# -------------------------------
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# -------------------------------
# Profit by Category
# -------------------------------
category_profit = df.groupby('Category')['Profit'].sum()

plt.figure()
category_profit.plot(kind='bar')
plt.title("Profit by Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()

# -------------------------------
# Top 10 Sub-Categories by Sales
# -------------------------------
top_products = (
    df.groupby('Sub-Category')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure()
top_products.plot(kind='barh')
plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Total Sales")
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

# -------------------------------
# Profit by Region
# -------------------------------
region_profit = df.groupby('Region')['Profit'].sum()

plt.figure()
region_profit.plot(kind='bar')
plt.title("Profit by Region")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("profit_by_region.png")
plt.show()

# -------------------------------
# Sales vs Profit Relationship
# -------------------------------
plt.figure()
plt.scatter(df['Sales'], df['Profit'])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("sales_vs_profit.png")
plt.show()

print("\nAnalysis Completed Successfully ✅")