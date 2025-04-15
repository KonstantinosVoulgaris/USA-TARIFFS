import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# URL to CSV file on GitHub
url = 'https://raw.githubusercontent.com/KonstantinosVoulgaris/USA-TARIFFS/main/Tariff%20Calculations%20plus%20Population.csv'

# Load the dataset
@st.cache
def load_data():
    df = pd.read_csv(url, sep=';')
    return df

df = load_data()

# Streamlit App
st.title('USA Tariffs and Population Analysis')

# Display first few rows of data
if st.checkbox('Show raw data'):
    st.write(df)

# Data Cleaning
df['Tariff'] = df['Tariff'].fillna(0)  # Fill NaN in 'Tariff' with 0
required_columns = ['Country', 'Population']
df = df.dropna(subset=required_columns)  # Drop rows with missing required columns
df = df.drop_duplicates()  # Remove duplicates

# Display cleaned data
st.subheader("Cleaned Data")
st.write(df)

# Basic Statistical Summary
st.subheader("Basic Statistical Summary")
st.write(df.describe())

# Grouped Analysis (Average Tariff per Region)
if 'Region' in df.columns and 'Tariff' in df.columns:
    region_avg_tariff = df.groupby('Region')['Tariff'].mean().sort_values(ascending=False)
    st.subheader("Average Tariff per Region")
    st.write(region_avg_tariff)
else:
    st.info("ℹ 'Region' and 'Tariff' columns not found for grouped analysis.")

# Visualization
if 'Region' in df.columns and 'Tariff' in df.columns:
    st.subheader("Average Tariff per Region - Bar Chart")
    fig, ax = plt.subplots(figsize=(10, 6))
    region_avg_tariff.plot(kind='bar', ax=ax)
    plt.ylabel('Average Tariff')
    plt.xlabel('Region')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
