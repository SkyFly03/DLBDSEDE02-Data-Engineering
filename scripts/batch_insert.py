# Inserts cleaned air_quality data into PostgreSQL in batches
# Uses SQLAlchemy engine and reads from air_quality_cleaned.csv

import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("data/air_quality_cleaned.csv")

# Connect to PostgreSQL
# Real credentials used for local execution only (remove before uploading to GitHub)
USER     = "david"
PASSWORD = "david123"
HOST     = "localhost"
PORT     = 5432
DBNAME   = "sensordb"

database_url = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
engine = create_engine(database_url)

# Insert in batches
batch_size = 10000
for i in range(0, len(df), batch_size):
    batch = df.iloc[i:i + batch_size]
    batch.to_sql("air_quality", engine, if_exists='append', index=False)
    print(f"Inserted rows {i} to {i + len(batch) - 1}")

print("All data inserted successfully.")
