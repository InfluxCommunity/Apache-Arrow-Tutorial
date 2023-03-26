from influxdb_client import InfluxDBClient
from pandas import DataFrame as df
import pyarrow.dataset as ds
import pyarrow as pa

with InfluxDBClient(url="http://localhost:8086", token="edge", org="influxdb", debug=False) as client:
    query_api = client.query_api()
    query = '''
    import "influxdata/influxdb/sample"
    sample.data(set: "${dataset}")
        |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
        |> group() 
    '''
param = {'dataset': 'usgs'}
df = query_api.query_data_frame(query=query, params=param)


table = pa.Table.from_pandas(df)
print(table)
print("Saving to parquet files...")

# Drop result and table columns
table = table.drop(["result", "table"])
print(table)

# partitioning of your data in smaller chunks
ds.write_dataset(table, "usgs", format="parquet",
                 partitioning=ds.partitioning(
                    pa.schema([table.schema.field("_measurement")])
                ))


