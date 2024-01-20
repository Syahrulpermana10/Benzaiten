# spark_script.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Create a Spark session
spark = SparkSession.builder.master("local").appName("SparkJob").getOrCreate()

# Load CSV data
df = spark.read.csv("/opt/airflow/dags/fake_data.csv", header=True, inferSchema=True)

# Perform data transformations
df_transformed = df.withColumn(
    "amount_category",
    when(col("amount") > 500, "High").when(col("amount") > 200, "Medium").otherwise("Low")
)

# Save the result in Parquet format
df_transformed.write.parquet("/opt/airflow/dags/output_parquet_file.parquet")

# Stop the Spark session
spark.stop()