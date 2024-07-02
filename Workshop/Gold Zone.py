# Databricks notebook source
from pyspark.sql import SparkSession

def transform_and_write_to_gold(silver_path, gold_path, checkpoint_path):
    try:
        # Initialize Spark session
        spark = SparkSession.builder.getOrCreate()

        # Step 1: Infer schema from existing files in Silver layer
        static_df = spark.read.format("parquet").load(silver_path)
        inferred_schema = static_df.schema

        # Step 2: Apply the inferred schema to the streaming DataFrame
        silver_df = spark.readStream \
            .format("parquet") \
            .schema(inferred_schema) \
            .load(silver_path)

        # Transform the DataFrame
        gold_df = silver_df.select('DeviceId', 'Latitude', 'Longitude', 'time')

        # Write to Gold layer (Transformed data)
        query = gold_df.writeStream \
            .format("parquet") \
            .option("path", gold_path) \
            .option("checkpointLocation", checkpoint_path) \
            .start()

        query.awaitTermination()
    except Exception as e:
        print(f'An error occurred: {e}')

# Usage example
silver_path = "/mnt/silver"
gold_path = "/mnt/gold"
checkpoint_path = "/mnt/gold_checkpoint"

transform_and_write_to_gold(silver_path, gold_path, checkpoint_path)
