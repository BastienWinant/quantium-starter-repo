import os
import pandas as pd
from dash import Dash, html, callback, Output, Input, dcc
import plotly.express as px

DATA_FILEPATH = os.path.abspath('data/output.csv')

df = pd.read_csv(DATA_FILEPATH)


app = Dash()


dropdown_values = df.Region.unique().tolist()
dropdown_values.insert(0, 'all')

app.layout = [
  html.H1(children='Pink Morsel product sales', style={'textAlign': 'center'}),
  dcc.Dropdown(dropdown_values, 'all', id="dropdown-select"),
  dcc.Graph(id="graph-content")
]

@callback(
  Output("graph-content", "figure"),
  Input("dropdown-select", "value")
)
def update_graph(value):
  if value == "all":
    dff = df.copy().sort_values('Date')
  else:
    dff = df.loc[df.Region == value, :].sort_values('Date')
  return px.line(dff, x="Date", y="Sales")

if __name__=="__main__":
  app.run(debug=True)