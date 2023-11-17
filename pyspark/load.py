from pyspark.sql import SparkSession
import pyarrow as pa
from utility import timer
from utility import update_spark_log_level
import pyarrow.parquet as pq

dataset = pq.ParquetDataset('Pyspark/1/')
table = dataset.read()
df = table.to_pandas()


# create a spark session
spark = SparkSession.builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()

update_spark_log_level(spark, log_level='OFF')

spark.conf.set("spark.sql.execution.arrow.enabled", "true")
sdf = spark.createDataFrame(df)

sdf.show()

