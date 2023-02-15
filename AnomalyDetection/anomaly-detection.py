

from flightsql import FlightSQLClient
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from adtk.data import validate_series
from adtk.detector import LevelShiftAD
import plotly.graph_objects as go


# Read only token for demo purposes
token = "6mFPNdcEwrjQD9utxkkMS6BfmhJoMIYsHkI317EcGSCMZaTalYADf0zm6u4VqrBv5YiGvvOf5Qa8sYTVrDigeA=="
 
client = FlightSQLClient(host='eu-central-1-1.aws.cloud2.influxdata.com',
                        token=token,
                        metadata={'bucket-name': 'factory'},
                        features={'metadata-reflection': 'true'})

# Execute a query against InfluxDB's Flight SQL endpoint                         
#query = client.execute("SELECT * FROM iox.mqtt_consumer WHERE time > (NOW() - INTERVAL '1 DAY') ")

query = client.execute("SELECT \"machineID\", vibration, time FROM iox.machine_data WHERE time > (NOW() - INTERVAL '1 DAY') AND \"machineID\" = 'machine3'")

# Create reader to consume result
reader = client.do_get(query.endpoints[0].ticket)

# Read all data into a pyarrow.Table
Table = reader.read_all()
print(Table)


# Convert to Pandas DataFrame
df = Table.to_pandas().set_index("time")
df = df.drop(columns=["machineID"])

# Create a Dash app
app = Dash(__name__)

# Create a plotly express figure (Line grah of raw Co2 Levels )

s_train = validate_series(df)
level_shift_ad = LevelShiftAD(c=6.0, side='both', window=5)
anomalies = level_shift_ad.fit_detect(s_train, return_list=False).rename(columns={"vibration": "anomalies"})


df = df.merge(anomalies, on="time", how="left")
df["anomalies"] = df["anomalies"].fillna(0).astype(int)
print(df)

fig1 = px.line(df, y="vibration", title='Vibration Levels')

# Create spike line
spikes_x = df[df['anomalies'] == 1].index
spikes_y = df[df['anomalies'] == 1]['vibration']
fig1.add_trace(go.Scatter(x=spikes_x, y=spikes_y, mode='markers', marker=dict(size=10)))

app.layout = html.Div(children=[
    html.H1(children='Vibration Levels of Machines'),

    html.Div(children='''
        Demo of PyArrow and Dash
    '''),

    dcc.Graph(
        id='raw-vibration',
        figure=fig1
    )
    
])

if __name__ == '__main__':
    app.run_server(debug=True)