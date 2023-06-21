import flightsql.sqlalchemy
from sqlalchemy import func, select
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import MetaData, Table

token = ""
host = "eu-central-1-1.aws.cloud2.influxdata.com"
bucket = "mlops"

engine = create_engine(f"datafusion+flightsql://{host}:443?bucket-name={bucket}&token={token}")

runs = Table("BW_Inference_results", MetaData(bind=engine), autoload=True)
count = select([func.count("*")], from_obj=runs).scalar()
print("runs count:", count)
print("columns:", [(r.name, r.type) for r in runs.columns])

# Reflection
metadata = MetaData(schema="iox")
metadata.reflect(bind=engine)
print("tables:", [table for table in metadata.sorted_tables])