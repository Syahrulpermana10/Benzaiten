# spark_dag.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'spark_job_dag',
    default_args=default_args,
    description='A simple Apache Spark DAG',
    schedule_interval='@daily',
)

# SparkSubmitOperator to submit the Spark job
spark_task = SparkSubmitOperator(
    task_id='spark_task',
    conn_id='spark_default',  # Assuming you've configured a Spark connection in Airflow
    application="/opt/airflow/spark_script.py",
    total_executor_cores='2',
    executor_cores='1',
    executor_memory='2g',
    num_executors='1',
    name='spark_job',
    verbose=False,
    dag=dag,
)

# Add the following line to make the DAG wait for the Spark job to finish
spark_task.dag = dag

# Define the order of tasks
spark_task