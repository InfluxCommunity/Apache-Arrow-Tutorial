from pyspark.sql import SparkSession
import pyarrow as pa
from flightsql import FlightSQLClient
from utility import timer
from utility import update_spark_log_level



# Read only token for demo purposes
token = "6mFPNdcEwrjQD9utxkkMS6BfmhJoMIYsHkI317EcGSCMZaTalYADf0zm6u4VqrBv5YiGvvOf5Qa8sYTVrDigeA=="
 
client = FlightSQLClient(host='eu-central-1-1.aws.cloud2.influxdata.com',
                        token=token,
                        metadata={'bucket-name': 'factory'},
                        features={'metadata-reflection': 'true'})
 
# Execute a query against InfluxDB's Flight SQL endpoint                        
query = client.execute("SELECT * FROM iox.machine_data WHERE time > (NOW() - INTERVAL '1 DAY')")
 
# Create reader to consume result
reader = client.do_get(query.endpoints[0].ticket)
 
# Read all data into a pyarrow.Tablef
Table = reader.read_all()


# create a spark session
spark = spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("") \
    .getOrCreate()
update_spark_log_level(spark, log_level='OFF')

#spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

print('''
#######################
#######################
#######################
''')
# create a Spark DataFrame from the Arrow Table
with timer() as timer:
    df = spark.createDataFrame(Table.to_pandas())
# show the contents of the DataFrame
df.show()