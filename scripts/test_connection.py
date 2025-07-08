# This script tests the database connection.
# Real credentials are intentionally masked to follow best practices and protect sensitive information.
# Replace the placeholder values below with your own local credentials before running.

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

USER     = "your_username"      
PASSWORD = "your_password"     
HOST     = "localhost"       
PORT     = 5432                            
DBNAME   = "your_database"           

# Construct the database URL  
database_url = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# Establish the connection engine using the constructed database URL
try:
    engine = create_engine(database_url)
    with engine.connect() as conn:
        print("Connection successful.")
except OperationalError as e:
    print("Connection failed:", e)