from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Set your InfluxDB credentials
url = "https://us-east-1-1.aws.cloud2.influxdata.com"
token = "JONCuM8MiccC974Zo2lAc5sRQndfNi_hlqYQmxSR5S3m3Uaogl6fW6WlkTM0erxPvNNBIL7W2eZanHbMqDIjfA=="
org = "28d1f2f565460a6c"
bucket_name = "new-bucket"

# Connect to the InfluxDB instance
client = InfluxDBClient(url=url, token=token)

# Create a new bucket
buckets_api = client.buckets_api()
bucket = buckets_api.create_bucket(bucket_name=bucket_name, org_id=org)

# Prepare sample data
sample_data = [
    {
        "measurement": "sensors",
        "tags": {"location": "kitchen"},
        "fields": {"temp": 23.5},
    },
    {
        "measurement": "sensors",
        "tags": {"location": "bedroom"},
        "fields": {"temp": 22.1},
    },
    {
        "measurement": "sensors",
        "tags": {"location": "kitchen"},
        "fields": {"humid": 52.3},
    },
    {
        "measurement": "sensors",
        "tags": {"location": "bedroom"},
        "fields": {"humid": 48.2},
    },
]

# Write sample data to the new bucket
write_api = client.write_api(write_options=SYNCHRONOUS)

write_api.write(bucket=bucket_name, org=org, record=sample_data)

print(f"Sample data written to '{bucket_name}' bucket.")

# Close the client
client.__del__()