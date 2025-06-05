import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Sample_Sales_Data (2).csv')

# --- Data Cleaning ---
# Convert 'Order Date' to datetime objects
df['Order Date'] = pd.to_datetime(df['Order Date'])

# --- Initial Data Inspection ---
print("--- Initial Data Inspection ---")
print("\nFirst 5 rows of the dataset:")
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nColumn information:")
print(df.info())

print("\nDescriptive statistics for numerical columns:")
print(df.describe().to_markdown(numalign="left", stralign="left"))

# --- Key Performance Indicators (KPIs) ---
print("\n--- Key Performance Indicators (KPIs) ---")

# Total Sales
total_sales = df['Sales'].sum()
print(f"Total Sales: ${total_sales:,.2f}")

# Total Profit
total_profit = df['Profit'].sum()
print(f"Total Profit: ${total_profit:,.2f}")

# Average Sales per Order
avg_sales_per_order = df['Sales'].mean()
print(f"Average Sales per Order: ${avg_sales_per_order:,.2f}")

# Average Profit per Order
avg_profit_per_order = df['Profit'].mean()
print(f"Average Profit per Order: ${avg_profit_per_order:,.2f}")

# Profit Margin
profit_margin = (total_profit / total_sales) * 100 if total_sales > 0 else 0
print(f"Profit Margin: {profit_margin:.2f}%")

# --- Categorical Column Analysis ---
print("\n--- Categorical Column Value Counts ---")
for col in ['Region', 'Category', 'Sub-Category', 'Customer Name']:
    print(f"\nValue counts for '{col}':")
    print(df[col].value_counts().to_markdown(numalign="left", stralign="left"))

# --- Data Visualization ---
print("\n--- Data Visualizations ---")
# Set a style for the plots
sns.set_style("whitegrid")

# 1. Sales by Region
plt.figure(figsize=(8, 5))
region_sales = df.groupby('Region')['Sales'].sum().reset_index()
sns.barplot(x='Region', y='Sales', data=region_sales, palette='viridis')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# 2. Profit by Category
plt.figure(figsize=(10, 6))
category_profit = df.groupby('Category')['Profit'].sum().reset_index()
sns.barplot(x='Category', y='Profit', data=category_profit, palette='magma')
plt.title('Total Profit by Category')
plt.xlabel('Category')
plt.ylabel('Total Profit')
plt.tight_layout()
plt.show()

# 3. Sales vs. Quantity (Scatter Plot)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Quantity', y='Sales', data=df, hue='Category', s=100, alpha=0.8)
plt.title('Sales vs. Quantity')
plt.xlabel('Quantity')
plt.ylabel('Sales')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 4. Profit vs. Sales (Scatter Plot)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Sales', y='Profit', data=df, hue='Category', s=100, alpha=0.8)
plt.title('Profit vs. Sales')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()