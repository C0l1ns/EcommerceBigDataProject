import pyspark.sql.types as t


def get_dataset_schema():
    return t.StructType(
        [
            t.StructField("event_time", t.TimestampType(), True),
            t.StructField("event_type", t.StringType(), True),
            t.StructField("product_id", t.LongType(), True),
            t.StructField("category_id", t.LongType(), True),
            t.StructField("category_code", t.StringType(), True),
            t.StructField("brand", t.StringType(), True),
            t.StructField("price", t.DoubleType(), True),
            t.StructField("user_id", t.LongType(), True),
            t.StructField("user_session", t.StringType(), True),
        ]
    )
