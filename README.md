# Benzaiten
Project Overview:
The project focuses on improving fraud detection capabilities through efficient data engineering using Apache Spark, Apache Airflow, and Docker. The integration of these technologies enables a scalable and automated approach to fraud detection, ensuring timely and accurate identification of suspicious activities.

Key Components:
Airflow DAG (Directed Acyclic Graph):

File: example_dag.py
Description:
Defines an Airflow DAG named 'spark_job_dag' for scheduling Spark jobs.
Utilizes SparkSubmitOperator to submit Spark jobs with specified configurations.
Schedules the DAG to run daily.
Environment Variables:

File: .env
Variables:
AIRFLOW_UID: User ID for Airflow container.
AIRFLOW_IMAGE_NAME: Apache Airflow Docker image version.
AIRFLOW_PROJ_DIR: Project directory.
PGHOST, PGDATABASE, PGUSER, PGPASSWORD: PostgreSQL database connection details.
Docker Compose Configuration:

File: docker-compose.yaml
Services:
airflow: Airflow container with environment variable configurations and volume mounts.
postgres: PostgreSQL container for database storage.
spark: Spark container configured as a master node.
Dockerfile:

File: Dockerfile
Description:
Utilizes the Apache Airflow version 2.1.2 as the base image.
Installs necessary dependencies specified in requirements.txt.
Copies the Spark script (spark_script.py) to the Airflow container.
Reverts user permissions to Airflow user.
Makefile:

File: Makefile
Commands:
start-airflow: Starts the Airflow container in detached mode.
stop-airflow: Stops the Airflow container.
restart-airflow: Restarts the Airflow container.
Requirements File:

File: requirements.txt
Library: pyspark==3.1.2
Description:
Lists the required Python libraries for the project.
Spark Script:

File: spark_script.py
Description:
Utilizes PySpark to create a Spark session.
Reads CSV data (fake_data.csv) into a Spark DataFrame.
Performs data transformations, categorizing amounts into 'High,' 'Medium,' or 'Low.'
Writes the transformed data into Parquet format.
Expected Output:
Automated execution of the Airflow DAG, triggering the Spark job for fraud detection.
Transformed data stored in Parquet format for further analysis.
Improved fraud detection capabilities through scalable and automated data engineering.
