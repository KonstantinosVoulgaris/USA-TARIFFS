# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# URL του CSV αρχείου στο GitHub
url = 'https://raw.githubusercontent.com/KonstantinosVoulgaris/USA-TARIFFS/main/Tariff%20Calculations%20plus%20Population.csv'

# Ανάγνωση του CSV από το GitHub
df = pd.read_csv(url, sep=';')

# Πρώτες γραμμές του dataset
print(df.head())

# Optional: Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Step 4: Initial Dataset Info
print("\nShape of dataset:", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nMissing Values:\n", df.isnull().sum())

# Step 5: Data Cleaning

# Fill NaN in 'Tariff' with 0 if it exists
if 'Tariff' in df.columns:
    df['Tariff'] = df['Tariff'].fillna(0)

# Drop rows missing critical fields (e.g., Country, Population)
required_columns = ['Country', 'Population']
existing_required = [col for col in required_columns if col in df.columns]
df = df.dropna(subset=existing_required)

# Drop duplicate rows
df = df.drop_duplicates()

print("\nData cleaned. New shape:", df.shape)

# Step 6: Basic Statistical Summary
print(df.describe())

# Step 7: Grouped Analysis (if applicable)
if 'Region' in df.columns and 'Tariff' in df.columns:
    region_avg_tariff = df.groupby('Region')['Tariff'].mean().sort_values(ascending=False)
    print("\nAverage Tariff per Region:\n", region_avg_tariff)
else:
    print("\nℹ 'Region' and 'Tariff' columns not found for grouped analysis.")

# Step 8: Visualization (Optional)
if 'Region' in df.columns and 'Tariff' in df.columns:
    region_avg_tariff.plot(kind='bar', figsize=(10, 6), title='Average Tariff per Region')
    plt.ylabel('Average Tariff')
    plt.xlabel('Region')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()