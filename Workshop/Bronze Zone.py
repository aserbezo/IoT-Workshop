# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

dbutils.widgets.text("storage_access_key", "", "Storage Access Key")
dbutils.widgets.text("connectionString", "", "connectionStringEventHub")

# COMMAND ----------

storage_account_name = "storageiottest1"
access_key = dbutils.widgets.get("storage_access_key")

def mount_containers():
    try:
        dbutils.fs.mount(
            source=f"wasbs://bronze@{storage_account_name}.blob.core.windows.net/",
            mount_point="/mnt/bronze",
            extra_configs={f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net": access_key}
        )
        print('Bronze container mounted successfully.')
        
        dbutils.fs.mount(
            source=f"wasbs://silver@{storage_account_name}.blob.core.windows.net/",
            mount_point="/mnt/silver",
            extra_configs={f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net": access_key}
        )
        print('Silver container mounted successfully.')

        dbutils.fs.mount(
            source=f"wasbs://gold@{storage_account_name}.blob.core.windows.net/",
            mount_point="/mnt/gold",
            extra_configs={f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net": access_key}
        )
        print('Gold container mounted successfully.')

    except Exception as e:
        error_message = str(e)
        if "Directory already mounted" in error_message:
            print('Container is already uploaded and mounted.')
        else:
            print(f'An error occurred: {e}')
    finally:
        print('Mounting process completed. Check if all containers are mounted correctly or already mounted.')
        
        


mount_containers()

# COMMAND ----------

# MAGIC %md ## Read From Event Hub and ingest the data in Bronze zone

# COMMAND ----------

from pyspark.sql import SparkSession

def write_to_bronze(connection_string, bronze_path, checkpoint_path):
    try:
        # Initialize Spark session
        spark = SparkSession.builder.getOrCreate()
        
        # Configure Event Hubs connection
        ehConf = {}
        ehConf['eventhubs.connectionString'] = spark.sparkContext._jvm.org.apache.spark.eventhubs.EventHubsUtils.encrypt(connection_string)
        print('Connection is Successful!!!')
        
        # Read stream from Event Hubs
        parsedDF = spark.readStream.format("eventhubs").options(**ehConf).load()
        parsedDF = parsedDF.withColumn("body", parsedDF["body"].cast("string")).select('body')
        
        # Write to Bronze layer (Raw data)
        query = parsedDF.writeStream \
            .format("parquet") \
            .option("path", bronze_path) \
            .option("checkpointLocation", checkpoint_path) \
            .start()
        
        # Await termination to keep the stream running
        query.awaitTermination()
    except Exception as e:
        print(f'An error occurred: {e}')

# Usage example
connection_string = dbutils.widgets.get("connectionString")
bronze_path = "/mnt/bronze"
checkpoint_path = "/mnt/bronze_checkpoint"

write_to_bronze(connection_string, bronze_path, checkpoint_path)
