# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType,TimestampType

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType, TimestampType

def process_and_write_to_silver(bronze_path, silver_path, checkpoint_path):
    try:
        # Initialize Spark session
        spark = SparkSession.builder.getOrCreate()
        
        # Step 1: Infer schema from existing files
        static_df = spark.read.format("parquet").load(bronze_path)
        inferred_schema = static_df.schema
        
        # Step 2: Apply the inferred schema to the streaming DataFrame
        bronze_df = spark.readStream \
            .format("parquet") \
            .schema(inferred_schema) \
            .load(bronze_path)
        
        # Define a schema for transformation
        schema = StructType([
            StructField("temp", IntegerType()),
            StructField("tire_press", IntegerType()),
            StructField("speed", IntegerType()),
            StructField("alert", StringType()),
            StructField("Latitude", DoubleType(), True),
            StructField("Longitude", DoubleType(), True),
            StructField("DeviceId", StringType()),
            StructField("time", TimestampType())
        ])
        
        # Transform the DataFrame
        silver_df = transform_dataframe(bronze_df, schema)
        
        # Write to Silver layer (Transformed data)
        query = silver_df.writeStream \
            .format("parquet") \
            .option("path", silver_path) \
            .option("checkpointLocation", checkpoint_path) \
            .start()
        
        # Await termination to keep the stream running
        query.awaitTermination()
    except Exception as e:
        print(f'An error occurred: {e}')

def transform_dataframe(df, schema):
    df = df.withColumn("parsed", from_json("body", schema))
    
    # Now extract the values into separate columns
    df = df.select(
        col("parsed.temp").alias("temp"),
        col("parsed.tire_press").alias("tire_press"),
        col("parsed.speed").alias("speed"),
        col("parsed.alert").alias("alert"),
        col("parsed.Latitude").alias("Latitude"),
        col("parsed.Longitude").alias("Longitude"),
        col("parsed.DeviceId").alias("DeviceId"),
        col("parsed.time").alias("time")
    )
    
    df = df.withColumn("Fahrenheit", col("temp") * 9 / 5 + 32)
    return df

# Usage example
bronze_path = "/mnt/bronze"
silver_path = "/mnt/silver"
checkpoint_path = "/mnt/silver_checkpoint"

process_and_write_to_silver(bronze_path, silver_path, checkpoint_path)


# COMMAND ----------


