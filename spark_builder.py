from pyspark.sql import SparkSession


def build_spark_session():
    return (
        SparkSession.builder.config("spark.executor.memory", "8g")
        # .config("spark.local.dir", "d:\\spark-tmp\\tmp ")
        .getOrCreate()
    )
