from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('processed_data.csv', names=['sales', 'date', 'region'])
df.sort_values('date', inplace=True)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pink Morsel Sales', style={'textAlign':'center'}),
    dcc.Dropdown(df.region.unique(), 'north', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.region==value]
    return px.line(dff, x='date', y='sales')

if __name__ == '__main__':
    app.run(debug=True)