# Script: recreate_table.py
# Purpose: Drops and recreates the air_quality table in PostgreSQL
# - Connects to the database
# - Defines table schema with appropriate data types
# - Ensures a clean and consistent structure for batch insertion

from sqlalchemy import create_engine, text

# Real credentials are masked for security
engine = create_engine("postgresql://your_username:your_password@localhost:5432/your_database")

with engine.begin() as conn:  # <-- note: begin() instead of connect()
    conn.execute(text("DROP TABLE IF EXISTS air_quality"))

    conn.execute(text("""
        CREATE TABLE air_quality (
            stationid TEXT,
            datetime TIMESTAMP,
            pm25 FLOAT,
            pm10 FLOAT,
            no FLOAT,
            no2 FLOAT,
            nox FLOAT,
            nh3 FLOAT,
            co FLOAT,
            so2 FLOAT,
            o3 FLOAT,
            benzene FLOAT,
            toluene FLOAT,
            xylene FLOAT,
            aqi FLOAT,
            aqi_bucket TEXT,
            data_source TEXT,
            ingestion_date TIMESTAMP
        );
    """))

print("Table 'air_quality' recreated.")
