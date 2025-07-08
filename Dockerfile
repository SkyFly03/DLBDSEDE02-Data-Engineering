# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy scripts and data
COPY scripts/ scripts/
COPY data/ data/

# Default action: run the batch insert
CMD ["python", "scripts/batch_insert.py"]
