# Prints column names from station_hour.csv
# Useful for verifying schema before cleaning or ingestion

import pandas as pd

df = pd.read_csv("data/station_hour.csv")
print(df.columns.tolist())
