# DLBDSEDE02 - Data Engineering Project 
## Task 1: Choose a suitable database and store the data in batches ![image](https://github.com/user-attachments/assets/3aff3d58-18b9-45d9-8f60-27e15c71a301) 


## Objective

The goal of this project is to build a batch data ingestion system for environmental sensor data. The system includes data cleaning, transformation, and storage into a 
PostgreSQL database using Docker for portability and reproducibility.

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
    A[(  **Select Dataset**<br/>Raw CSV files  )] --> B[(  **Clean Data**<br/>clean_data.py  )]
    B --> C[(  **Setup Database**<br/>recreate_table.py<br/>schema.sql  )]
    C --> D[(  **Insert Batch**<br/>batch_insert.py  )]
    D --> E[(  **Validate Ingestion**<br/>Run SQL query  )]
    E --> F[(  **Containerization**<br/>docker-compose.yml<br/>Dockerfile  )]
    F --> G[(  **Document Project**<br/>#<br/>README.md  )]

    %% Node colors and font size
    style A fill:#fff9b1,stroke:#eec900,stroke-width:4px,font-size:24px
    style B fill:#ffe0a3,stroke:#ffb347,stroke-width:4px,font-size:24px
    style C fill:#ffbfa3,stroke:#ff7f50,stroke-width:4px,font-size:24px
    style D fill:#ffb1c1,stroke:#ff4f81,stroke-width:4px,font-size:24px
    style E fill:#e1b1ff,stroke:#b266ff,stroke-width:4px,font-size:24px
    style F fill:#b1c7ff,stroke:#668cff,stroke-width:4px,font-size:24px
    style G fill:#6a9ce6,stroke:#2f5aa8,stroke-width:4px,font-size:24px
```

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
* Connection uses SQLAlchemy
* Batch size: 10,000 rows
 

### 5. Ingestion Validation


![image](https://github.com/user-attachments/assets/d321e1e4-ce14-4cb6-aae7-3e55a54768a0)
* `test_connection.py` verifies database credentials and connection
* A `SELECT COUNT(*)` query confirms that the records were successfully ingested

### 6. Containerization

  ![docker_ps](https://github.com/user-attachments/assets/57fe8020-e05f-489b-aa78-9d1fafe8df37)
* PostgreSQL runs in a Docker container via `docker-compose.yml`
* Consistent setup across systems without manual installation  
* Deployment supported to cloud platforms and horizontal scaling with tools like Kubernetes
* Flexible structure for future extensions as streaming or microservices

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
