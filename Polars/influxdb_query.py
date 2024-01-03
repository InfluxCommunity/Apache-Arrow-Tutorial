

import polars as pl
from influxdb_client_3 import InfluxDBClient3



client = InfluxDBClient3(
    token="",
    host="eu-central-1-1.aws.cloud2.influxdata.com",
    org="6a841c0c08328fb1")

sql = 'SELECT * FROM caught LIMIT 10'

table = client.query(database="pokemon-codex", query=sql, language='sql', mode='all')

df = pl.from_arrow(table)

print(df)

client.close()