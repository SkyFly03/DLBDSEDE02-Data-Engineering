# Script: clean_data.py
# Purpose: Cleans the raw station_hour.csv dataset by:
# - normalizing column names
# - converting date formats
# - dropping rows with missing PM2.5 and PM10 values
# - adding ingestion metadata
# - exporting cleaned data as air_quality_cleaned.csv

import pandas as pd

# Load raw CSV
df = pd.read_csv("data/station_hour.csv")

# Normalize column names
df.columns = [col.strip().lower().replace(".", "").replace(" ", "_") for col in df.columns]

# Convert datetime column
df['datetime'] = pd.to_datetime(df['datetime'])

# Drop rows with missing values in key sensor columns
df = df.dropna(subset=['pm25', 'pm10'])

# Add metadata
df['data_source'] = 'kaggle'
df['ingestion_date'] = pd.Timestamp.now()

# Save cleaned data
df.to_csv("data/air_quality_cleaned.csv", index=False)

print("Cleaned data saved to: data/air_quality_cleaned.csv")

