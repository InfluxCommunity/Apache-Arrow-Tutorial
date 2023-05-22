from opensky_api import OpenSkyApi
import pandas as pd
from influxdb_client  import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import time


# Read only token for demo purposes
token = ""
org = ""
db = ""
url= ""

influxdbClient = InfluxDBClient(url=url, token=token, org=org)
write_api = influxdbClient.write_api(write_options=SYNCHRONOUS)


# FLIGHTS
api = OpenSkyApi()
states = api.get_states()

total_row = 0
batch = 0
df_list = []


while True:
    timestamp = str(datetime.now())
    total_row = 0
    for s in states.states:
            if batch == 300:
                concatenated = pd.concat(df_list).infer_objects().fillna(method='pad')
                concatenated['sensors'] = concatenated['sensors'].fillna("None")
        
                concatenated = concatenated.convert_dtypes()

                batch = 0
                df_list = []
                   
                try: 
                       concatenated['time'] = pd.to_datetime(concatenated['time'])
                       write_api.write(bucket=db, record=concatenated, data_frame_measurement_name='flight', data_frame_tag_columns=['icao24', 'origin_country'], data_frame_timestamp_column='time' )
                except:
                    total_row -= 300
                        
           

            df = pd.DataFrame.from_dict(s.__dict__, orient='index' ).T
            df['time'] = timestamp
            df_list.append(df)
            batch += 1
            total_row += 1
    print(f"Inserted {total_row} rows")
    time.sleep(15)
    