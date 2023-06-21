

from flightsql import FlightSQLClient
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import pyarrow.dataset as ds



# Read only token for demo purposes
token = ""

client = FlightSQLClient(host='us-east-1-1.aws.cloud2.influxdata.com',
                         token=token,
                         metadata= {'bucket-name': 'C02-Demo'}
                         )

# Execute a query against InfluxDB's Flight SQL endpoint                         
#query = client.execute("SELECT * FROM iox.mqtt_consumer WHERE time > (NOW() - INTERVAL '1 DAY') ")

query = client.execute("SELECT * FROM iox.mqtt_consumer")

# Create reader to consume result
reader = client.do_get(query.endpoints[0].ticket)

# Read all data into a pyarrow.Table
Table = reader.read_all()
print(Table)


# Convert to Pandas DataFrame
df = Table.to_pandas()
df = df.sort_values(by="time")
print(df)

# Create a Dash app
app = Dash(__name__)

# Create a plotly express figure (Line grah of raw Co2 Levels )
fig1 = px.line(df, x="time", y="co2", color='location', title='Co2 Levels')

# PyArrow Aggregation
aggregation = Table.group_by("location").aggregate([("co2", "mean"), ("co2", "max"), ("co2", "min") ]).to_pandas()
# Reshape Data Frame
aggregation=pd.melt(aggregation,id_vars=['location'],var_name='aggregation', value_name='value')
fig2 = px.bar(aggregation, x="location", y="value", color='aggregation', barmode= 'group', title='Co2 min,max,mean')


app.layout = html.Div(children=[
    html.H1(children='Co2 Levels in the home'),

    html.Div(children='''
        Demo of PyArrow and Dash
    '''),

    dcc.Graph(
        id='raw-co2',
        figure=fig1
    ),
        dcc.Graph(
        id='aggregation-co2',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)