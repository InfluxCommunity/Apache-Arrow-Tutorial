

import polars as pl
from influxdb_client_3 import InfluxDBClient3,InfluxDBError,WriteOptions,write_client_options
import pandas as pd
import numpy as np
import random
import time


now = pd.Timestamp.now(tz='UTC').floor('ms')



class BatchingCallback(object):

    def success(self, conf, data: str):
        print(f"Written batch: {conf}, data: {data}")

    def error(self, conf, data: str, exception: InfluxDBError):
        print(f"Cannot write batch: {conf}, data: {data} due: {exception}")

    def retry(self, conf, data: str, exception: InfluxDBError):
        print(f"Retryable error occurs for batch: {conf}, data: {data} retry: {exception}")

callback = BatchingCallback()


write_options = WriteOptions(batch_size=1000,
                                        flush_interval=10_000,
                                        jitter_interval=2_000,
                                        retry_interval=5_000,
                                        max_retries=10,
                                        max_retry_delay=15_000,
                                        exponential_base=2, max_close_wait=900_000)

wco = write_client_options(success_callback=callback.success,
                          error_callback=callback.error,
                          retry_callback=callback.retry,
                          WriteOptions=write_options 
                        )

client = InfluxDBClient3(
    token="",
    host="eu-central-1-1.aws.cloud2.influxdata.com",
    org="6a841c0c08328fb1", enable_gzip=True, write_client_options=wco)


pl_df =pl.read_parquet('pokemon_100_000.parquet')

print(pl_df.columns)

print(pl_df)


client.write(database="pokemon-codex", record=pl_df, data_frame_measurement_name='caught', data_frame_tag_columns=['trainer', 'id', 'num'], data_frame_timestamp_column='timestamp')

client.close()