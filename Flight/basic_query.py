import pyarrow as pa
import json
from pyarrow.flight import FlightClient, Ticket, FlightCallOptions
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


# Define FLight Client
host = "eu-central-1-1.aws.cloud2.influxdata.com"
token = ""
flight_client = FlightClient(f"grpc+tls://{host}:443")
_options = FlightCallOptions(headers=[(b"authorization", f"Bearer {token}".encode('utf-8'))])


# Define Query (Please define your own query)
database = "INSERT"
query = "SELECT * FROM table WHERE time > (NOW() - INTERVAL '1 DAY') "
language = "sql"

ticket_data = {"database": database, "sql_query": query, "query_type": language}
ticket = Ticket(json.dumps(ticket_data).encode('utf-8'))
flight_reader = flight_client.do_get(ticket, _options)


# Read all data into a pyarrow.Table
table = flight_reader.read_all()

# Convert to Pandas DataFrame (requires pandas to be installed)
df = table.to_pandas()

# Create a Dash app
app = Dash(__name__)

# Create a plotly express figure (Line grah of raw Co2 Levels )
fig1 = px.line(df, x="time", y="co2", color='location', title='Co2 Levels')

# PyArrow Aggregation
aggregation = table.group_by("location").aggregate([("co2", "mean"), ("co2", "max"), ("co2", "min") ]).to_pandas()

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