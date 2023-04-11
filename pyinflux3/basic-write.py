import influxdb_client_3 as InfluxDBClient3
import pandas as pd
import numpy as np

client = InfluxDBClient3.InfluxDBClient3(token="spqIiWojlcbAQC-FotEltyPqKhlhppuo36DYc5RIXxZl3EM3nRvSDQ3Lc75tkjBlml__oG3bI199gG3IdVKYlw==",
                         host="eu-central-1-1.aws.cloud2.influxdata.com",
                         org="6a841c0c08328fb1",
                         namespace="test")



# Create a dataframe
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})


# Create a range of datetime values
dates = pd.date_range(start='2023-04-01', end='2023-04-11', freq='5min')

# Create a DataFrame with random data and datetime index
df = pd.DataFrame(np.random.randn(len(dates), 3), index=dates, columns=['Column 1', 'Column 2', 'Column 3'])
df['tagkey'] = 'Hello World'

print(df)

# Write the DataFrame to InfluxDB
client.write(df, data_frame_measurement_name='table', data_frame_tag_columns=['tagkey']) 