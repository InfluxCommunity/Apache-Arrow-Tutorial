from influxdb_client_3 import InfluxDBClient3, flight_client_options
from influxdb_client import InfluxDBClient, Point, WriteOptions
import certifi

fh = open(certifi.where(), "r")
cert = fh.read()
fh.close()


cloud_url = "eu-central-1-1.aws.cloud2.influxdata.com"
cloud_token = ""
cloud_org = ""
cloud_database= ""

local_url = ""
local_token = ""
local_org = ""
local_database= ""


cloud_client = InfluxDBClient3(host=cloud_url, token=cloud_token, org=cloud_org,
    flight_client_options=flight_client_options(tls_root_certs=cert))
local_client = InfluxDBClient(url=local_url, token=local_token, org=local_org)

query = '''SELECT * FROM "INSERT"'''
reader = cloud_client.query(query =query, language='influxql', mode='chunk', database=cloud_database)

try:
    while True:
        batch, buff = reader.read_chunk()
        df = batch.to_pandas()
        measurement = df.loc[0, 'iox::measurement']
        df = df.drop(columns=['iox::measurement']).set_index('time')

        print(df)

        with local_client.write_api(write_options=WriteOptions(batch_size=500,
                                                      flush_interval=10_000,
                                                      jitter_interval=2_000,
                                                      retry_interval=5_000,
                                                      max_retries=5,
                                                      max_retry_delay=30_000,
                                                      max_close_wait=300_000,
                                                      exponential_base=2)) as _write_client:

         _write_client.write(bucket=local_database, record=df, data_frame_measurement_name=measurement, data_frame_tag_columns=['location'])
except StopIteration:
    print("Data transfer complete")





