import os
import pandas as pd
from dash import Dash, html, callback, Output, Input, dcc, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc

DATA_FILEPATH = os.path.abspath('data/output.csv')

df = pd.read_csv(DATA_FILEPATH)

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets)

radio_values = df.Region.unique().tolist()
radio_values.insert(0, 'all')


app_title = html.H1(
  children='Pink Morsel product sales',
  style={'marginTop': '40px'})

radio_btns = dcc.RadioItems(options=radio_values, value='all', id='controls-and-radio-item', inline=True)
graph = dcc.Graph(id="graph-content")
data_table = dash_table.DataTable(data=df.to_dict('records'), page_size=11, style_table={'overflowX': 'auto'})

app.layout = [
  app_title,
  html.Hr(),
  html.Div(radio_btns),
  graph,
  data_table
]

@callback(
  Output("graph-content", "figure"),
  Input("controls-and-radio-item", "value")
)
def update_graph(value):
  if value == "all":
    dff = df.copy().sort_values('Date')
  else:
    dff = df.loc[df.Region == value, :].sort_values('Date')
  return px.line(dff, x="Date", y="Sales")

if __name__=="__main__":
  app.run(debug=True)