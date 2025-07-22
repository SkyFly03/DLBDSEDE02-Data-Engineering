# DLBDSEDE02 - Data Engineering Project 
## Task 1: Choose a suitable database and store the data in batches ![image](https://github.com/user-attachments/assets/3aff3d58-18b9-45d9-8f60-27e15c71a301) 

## Situation

A municipality is collecting environmental data from distributed sensors and plans to expand measurements (e.g., CO₂, noise) in the future. The system must handle structured data batches, adapt to new sensor types, and support scalable deployment across local and cloud environments. 

## Requirements & Technical Solutions

| Project Requirement                                                    | Technical Need                                        | Implemented Solution                                     |
|------------------------------------------------------------------------|--------------------------------------------------------|----------------------------------|
| Store large volumes of sensor data in batches                         | Structured, repeatable ingestion                      | **SQLAlchemy** – Manages schema creation and batch inserts via Python |
| Support additional sensor types in the future                         | Flexible, schema-adaptable storage                    | **PostgreSQL** – Relational DB with schema control and indexing       |
| Ensure the system works locally and in the cloud                      | Environment-independent deployment                    | **Docker** – Provides consistent runtime across platforms              |
| Minimize setup effort for all components                              | Automated service orchestration                       | **Docker Compose** – Starts database and scripts in one command        |
| Enable long-term scalability and easy maintenance                     | Modular, portable, open-source architecture           | **Open-source stack** – Easy to extend, version, and manage            |


## Technical Setup

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

## Technical Justification

- **Docker**: Provides consistent, isolated environments. Ensures the system runs identically on any machine or platform.
- **Docker Compose**: Orchestrates services (PostgreSQL + scripts) with one command. Manages networking and execution automatically.
- **PostgreSQL**: A relational database ideal for time-series sensor data. Supports indexing, structured queries, and future schema extension.
- **SQLAlchemy**: Handles table creation and batch inserts in reusable Python code. Enables schema control and maintainability.

## Rejected Alternatives

- **NoSQL databases** (e.g., MongoDB): Not suitable for structured sensor data that requires relational queries and schema enforcement.
- **MongoDB**: Does not offer full ACID compliance or efficient multi-dimensional indexing needed for scalable, time-based storage.

---
## Process Description

### 1. Dataset

* Dataset: Air Quality Data in India  
* Source: [Kaggle – Air Quality Data](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)  
* Description: The dataset includes hourly and daily air pollution measurements collected from various Indian cities. Parameters include PM2.5, PM10, NOx, SO2, O3, and AQI.

### 2. Data Cleaning

* `clean_data.py` processes `station_hour.csv`:
  - Normalizes column names
  - Converts datetime
  - Removes rows with missing PM2.5 or PM10
  - Adds metadata (source and ingestion timestamp)
  - Saves output as `air_quality_cleaned.csv`

### 3. Database Setup

* `recreate_table.py` connects to PostgreSQL and recreates the `air_quality` table with the proper schema
* `schema.sql` provides the same structure in raw SQL format

### 4. Batch Insertion

 ![image](https://github.com/user-attachments/assets/1ad436fc-dc32-49db-b9d3-95a7ec308355)
* `batch_insert.py` loads cleaned data and inserts it into PostgreSQL in chunks
* SQLAlchemy handles the database connection and insertion logic in Python
* Batch size: 10,000 rows

### 5. Ingestion Validation

![image](https://github.com/user-attachments/assets/d321e1e4-ce14-4cb6-aae7-3e55a54768a0)
* `test_connection.py` verifies database credentials and connection
* A `SELECT COUNT(*)` query confirms that the records were successfully ingested

### 6. Containerization

  ![docker_ps](https://github.com/user-attachments/assets/57fe8020-e05f-489b-aa78-9d1fafe8df37)
* PostgreSQL runs in a Docker container via `docker-compose.yml`
* Containers can be started, stopped, or replaced independently  
* The system can be run on any machine or deployed in cloud environments
* All components are version-controlled for reproducibility and easy migration

### 7. Documentatation

* in code and `README.md`
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

## Conclusion

This system demonstrates how a containerized, Python-driven ETL pipeline can efficiently store structured environmental data in batches. By combining PostgreSQL, Docker, and SQLAlchemy, the solution remains scalable, portable, and ready for future sensor expansion with minimal reconfiguration.
