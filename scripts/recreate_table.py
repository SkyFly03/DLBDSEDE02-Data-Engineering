from sqlalchemy import create_engine, text

engine = create_engine("postgresql://david:david123@localhost:5432/sensordb")

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