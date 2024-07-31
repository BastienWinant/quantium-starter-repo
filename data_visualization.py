import os
import pandas as pd
from dash import Dash, html, callback, Output, Input, dcc, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc

# read in the data
DATA_FILEPATH = os.path.abspath('data/output.csv')
df = pd.read_csv(DATA_FILEPATH)

# create app with theme
external_stylesheets = [dbc.themes.JOURNAL]
app = Dash(__name__, external_stylesheets=external_stylesheets)

def headerTitle():
  title = html.H1(
  children='Pink Morsel product sales',
  style={ "textAlign": "center"})

  return title

def radioBtns():
  radio_values = df.Region.unique().tolist()
  radio_values.insert(0, 'all')

  radio_btns = dcc.RadioItems(
    options=radio_values, value='all',
    id='controls-and-radio-item',
    style={"display": "flex", "justifyContent": "center", "gap": "2vw"},
    labelStyle={"display": "flex", "gap": ".25vw", "textTransform": "capitalize"})
  
  return radio_btns

def dataTable():
  data_table = dash_table.DataTable(
    data=df.to_dict('records'),
    style_cell={"border": "none", "padding": "20px 10px"},
    id="sales-table")
  
  return data_table

graph = dcc.Graph(id="graph-content")

def appLayout():
  return [
    html.Div(
      children=[
        html.Header(children=[headerTitle()], id="app-header"),
        html.Hr(),
        html.Section(
          children=[radioBtns()],
          id="graph-section"),
        html.Section(
          children=[graph],
          id="graph-container"
        ),
        html.Section(
          children=[dataTable()],
          id="data-table-container"
        )
      ],
      style={"display": "flex", "flexDirection": "column", "gap": "10px", "padding": "40px 6vw"},
      id="layout-container"
    )
  ]

app.layout = appLayout()

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

@callback(
  Output("sales-table", "data"),
  Input("controls-and-radio-item", "value")
)
def update_table(value):
  if value == "all":
    dff = df.copy().sort_values('Date')
  else:
    dff = df.loc[df.Region == value, :].sort_values('Date')
  return dff.to_dict('records')

if __name__=="__main__":
  app.run(debug=True)