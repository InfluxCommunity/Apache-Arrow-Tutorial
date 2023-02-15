from flightsql import FlightSQLClient

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
print(Table)
 
# Convert to Pandas DataFrame
df = Table.to_pandas()
df = df.sort_values(by="time")
print(df)