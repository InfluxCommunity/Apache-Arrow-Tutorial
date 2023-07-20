import influxdb_client_3 as InfluxDBClient3
import pandas as pd
import numpy as np
from influxdb_client_3 import write_options

client = InfluxDBClient3.InfluxDBClient3(token="",
                         host="",
                         org="",
                         database="flight2", enable_gzip=True, write_options=write_options(batch_size=500,
                                                      flush_interval=10_000,
                                                      jitter_interval=2_000,
                                                      retry_interval=5_000,
                                                      max_retries=5,
                                                      max_retry_delay=30_000,
                                                      max_close_wait=300_000,
                                                      exponential_base=2, write_type='batching'))



# Create a dataframe
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})


# Create a range of datetime values
dates = pd.date_range(start='2023-05-01', end='2023-05-29', freq='5min')

# Create a DataFrame with random data and datetime index
df = pd.DataFrame(np.random.randn(len(dates), 3), index=dates, columns=['Column 1', 'Column 2', 'Column 3'])
df['tagkey'] = 'Hello World'

print(df)

# Write the DataFrame to InfluxDB
client.write(df, data_frame_measurement_name='table3', data_frame_tag_columns=['tagkey']) 

# Query with influxQL 
table = client.query(query="SELECT * FROM table3 WHERE time > now() - 30d", language="influxql")
print(table.to_pandas())