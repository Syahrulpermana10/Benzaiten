# Dockerfile
# Use Apache Airflow image as the base image
FROM apache/airflow:2.1.2

# Set the user to root to be able to install dependencies
USER root

# Install the required dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy the Spark script file into the container
COPY spark_script.py /usr/local/airflow/spark_script.py

# Switch back to the airflow user
USER airflow  