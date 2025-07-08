-- schema.sql: Defines the table structure for air_quality data

DROP TABLE IF EXISTS air_quality;

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
