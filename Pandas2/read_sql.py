import flightsql.sqlalchemy
from sqlalchemy.engine import create_engine
import pandas as pd
from utility import timer
from flightsql import FlightSQLClient
import pandas as pd


token = "6mFPNdcEwrjQD9utxkkMS6BfmhJoMIYsHkI317EcGSCMZaTalYADf0zm6u4VqrBv5YiGvvOf5Qa8sYTVrDigeA=="
host = "eu-central-1-1.aws.cloud2.influxdata.com"
bucket = "factory"

engine = create_engine(f"datafusion+flightsql://{host}:443?bucket-name={bucket}&token={token}")

client = FlightSQLClient(host=host,
                        token=token,
                        metadata={'bucket-name': bucket})

with timer() as timer2:
    query = client.execute("SELECT * FROM iox.machine_data WHERE time > (NOW() - INTERVAL '1 DAY')")
        # Create reader to consume result
    reader = client.do_get(query.endpoints[0].ticket)
        # Read all data into a pyarrow.Table
    Table = reader.read_all()
    p = Table.to_pandas()
        #print(table)

with timer() as timer1:
    table = pd.read_sql("SELECT * FROM iox.machine_data WHERE time > (NOW() - INTERVAL '1 DAY')", engine, dtype_backend="pyarrow")




