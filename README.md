## ▸ Project Overview
- **Batch ingestion pipeline:** containerized Python workflow for environmental sensor data  
- **Database integration:** PostgreSQL with structured schema management  
- **Reproducible execution:** Docker-based setup for consistent runs  

## ▸ Why this project matters
- **Core data engineering principles:** batch ingestion, validation, persistence  
- **Analytics-ready design:** structured data storage for downstream use  
- **Scalable foundation:** ETL-style pipeline aligned with real-world practice  

---
---

# DLBDSEDE02 – Data Engineering Project  
## Task 1: Batch Storage System for Environmental Sensor Data

---

## Challenges & Technical Solutions

This system was built to store growing sensor data in a way that is scalable, maintainable, and easy to deploy. The following tools were selected based on technical strengths:

- **PostgreSQL** stores structured sensor data and allows schema adjustments, making it a reliable choice for growing datasets and fast querying *(scalable, maintainable)*

- **SQLAlchemy** defines and manages the schema in Python, which simplifies changes and integrates well into the data pipeline *(maintainable)*

- **pandas** loads large datasets in chunks, allowing batch processing that reduces memory usage and improves speed *(scalable)*

- **Containerization** allows the system to run consistently across environments, isolate dependencies, and simplify deployment *(portable, reproducible)*
  
  → Implemented using:
    - **Docker** to package the environment as reusable containers
    - **Docker Compose** to run all components together and manage service interaction *(maintainable, portable)*
      
- **Version Control** ensures all scripts and setup files are tracked and accessible for reuse or modification  
  → Implemented via a public GitHub repository *(maintainable, reproducible)*

---

## Technical Setup
Follow these steps to bootstrap and run the batch ingestion pipeline locally.

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
<img width="2138" height="342" alt="image" src="https://github.com/user-attachments/assets/cdffdb0a-8790-44e7-bf4a-c34196ef38ea" />

---
## Process Description

### 1. Dataset

* Source: [Kaggle – Air Quality Data](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)
* Hourly air quality data collected from Indian cities 
* Includes PM2.5, PM10, NOx, SO2, O3, and AQI values
  
### 2. Data Cleaning (*`clean_data.py`*)

* Drops incomplete rows (PM2.5 or PM10 missing)
* Standardizes column names and converts timestamp formats
* Adds metadata fields like ingestion time and data source
* Saves a cleaned version as `air_quality_cleaned.csv`

### 3. Database Setup (*`recreate_table.py`* / *`schema.sql`*)

* Defines a PostgreSQL table matching the cleaned dataset
* Uses SQLAlchemy to create the table from Python, allowing dynamic schema management
* Provides an optional schema.sql file for manual SQL-based table creation

### 4. Batch Insertion (*`batch_insert.py`*)

 ![image](https://github.com/user-attachments/assets/1ad436fc-dc32-49db-b9d3-95a7ec308355)
* Loads the cleaned CSV in chunks of 10,000 rows using `pandas.read_csv(chunksize=...)`
* Inserts each chunk into the database using `psycopg2.extras.execute_batch()` through SQLAlchemy
* Batch processing improves performance and avoids memory overload on large files
  
### 5. Ingestion Validation (*`test_connection.py`*)

![image](https://github.com/user-attachments/assets/d321e1e4-ce14-4cb6-aae7-3e55a54768a0)
* Verifies database credentials and connection
* Confirms successful ingestion with `SELECT COUNT(*)` query

### 6. Containerization (*`docker-compose.yml`*)

  ![docker_ps](https://github.com/user-attachments/assets/57fe8020-e05f-489b-aa78-9d1fafe8df37)
* Runs PostgreSQL and Python scripts in separate containers
* `docker-compose.yml` defines both services and manages networking between them
* The full system is launched with one command: `docker-compose up -d`
* System can be deployed consistently on any machine or cloud

### 7. Documentation

* All code, schema, and setup files are version-controlled in GitHub
* System usage is explained in this `README.md`
---

## Project Structure

```
DLBDSEDE02-Data-Engineering/
├── data/
│   └── (large .csv files excluded from repo)
├── images/
│   ├── insert_output.png (2)
│   ├── count_rows.png
│   └── docker_ps.png
├── scripts/
│   ├── batch_insert.py 
│   ├── check_columns.py 
│   ├── clean_data.py
│   ├── recreate_table.py
│   └── test_connection.py
├── .gitignore 
├── Dockerfile
├── README.md
├── docker-compose.yml
├── requirements.txt
└── schema.sql
```
---
## Results & Key Outputs
See the `images/` folder for visual confirmation.
- Tables created in PostgreSQL with ingested environmental sensor records
- Batch insert performance screenshot
- Connection and validation checks passing

## Conclusion

- This project shows how a containerized Python-based pipeline can clean and store structured sensor data in batches. 
- Using PostgreSQL, Docker, and SQLAlchemy, the system is easy to deploy, extend, and adapt to future data requirements.

