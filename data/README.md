# DLBDSEDE02 - Data Engineering Project 
## Task 1: Choose a suitable database and store the data in batches ![image](https://github.com/user-attachments/assets/3aff3d58-18b9-45d9-8f60-27e15c71a301) 


## Objective

The goal of this project is to build a batch data ingestion system for environmental sensor data. The system includes data cleaning, transformation, and storage into a 
PostgreSQL database using Docker to ensure portability and reproducibility.

## Data Source

* Dataset: Air Quality Data in India  
* Source: [Kaggle – Air Quality Data](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)  
* Description: The dataset includes hourly and daily air pollution measurements collected from various Indian cities. Parameters include PM2.5, PM10, NOx, SO2, O3, and AQI.

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/SkyFly03/DLBDSEDE02-Data-Engineering.git
   cd DLBDSEDE02-Data-Engineering
   ```

2. Create and activate the virtual environment:
   ```
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Start PostgreSQL container using Docker:
   ```
   docker-compose up -d
   ```

## Workflow Overview

```mermaid
graph LR
    A[  Raw CSV Files  ] --> B[  clean_data.py  ]
    B --> C[  air_quality_cleaned.csv  ]
    C --> D[  batch_insert.py  ]
    D --> E[(  PostgreSQL via Docker  )]
    E --> F["  SELECT COUNT(*) to verify  "]

    %% Node colors and font size for bigger boxes
    style A fill:#fff9b1,stroke:#eec900,stroke-width:4px,font-size:24px
    style B fill:#ffe0a3,stroke:#ffb347,stroke-width:4px,font-size:24px
    style C fill:#ffbfa3,stroke:#ff7f50,stroke-width:4px,font-size:24px
    style D fill:#ffb1c1,stroke:#ff4f81,stroke-width:4px,font-size:24px
    style E fill:#e1b1ff,stroke:#b266ff,stroke-width:4px,font-size:24px
    style F fill:#b1c7ff,stroke:#668cff,stroke-width:4px,font-size:24px
```
## Process Description

### 1. Data Cleaning

* `clean_data.py` processes `station_hour.csv`:
  - Normalizes column names
  - Converts datetime
  - Removes rows with missing PM2.5 or PM10
  - Adds metadata (source and ingestion timestamp)
  - Saves output as `air_quality_cleaned.csv`

### 2. Database Setup

* `recreate_table.py` connects to PostgreSQL and recreates the `air_quality` table with the proper schema
* `schema.sql` provides the same structure in raw SQL format

### 3. Batch Insertion

* `batch_insert.py` loads cleaned data and inserts it into PostgreSQL in chunks
* Connection uses SQLAlchemy
* Batch size: 10,000 rows

### 4. Validation

* `test_connection.py` verifies database credentials and connection
* A `SELECT COUNT(*)` query confirms that the records were successfully ingested

## Project Structure

```
DLBDSEDE02-Data-Engineering/
├── data/
│   └── (large .csv files excluded from repo)
├── images/
│   ├── docker_ps.png
│   ├── insert_output.png
│   └── count_rows.png
├── scripts/
│   ├── clean_data.py
│   ├── recreate_table.py
│   ├── batch_insert.py
│   ├── check_columns.py
│   └── test_connection.py
├── schema.sql
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .gitignore
```

## Project Summary

- Identified PostgreSQL as a scalable, reliable, and cloud-ready database solution
- Used Docker for portability
- Selected a dataset with extensible structure to support future sensor types 

- Built a local batch data ingestion pipeline using Python and Docker
- Implemented modular scripts for cleaning, table creation, and data insertion
- Validated ingestion process with screenshots and row count checks
