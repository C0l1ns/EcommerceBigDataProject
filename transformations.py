import pyspark.sql.functions as f

from spark_builder import build_spark_session
from schema import get_dataset_schema

from pyspark.sql import SparkSession


def trasform_bronze_silver(
    spark: SparkSession, bronze_path="./bronze/*.csv", silver_path="./silver/"
):
    schema = get_dataset_schema()

    bronze_df = spark.read.csv(path=bronze_path, schema=schema).limit(20000000)

    silver_df = bronze_df.drop_duplicates()
    silver_df = silver_df.filter(f.col("event_time").isNotNull())

    silver_df.write.format("parquet").mode("overwrite").save(silver_path)
