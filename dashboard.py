from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('processed_data.csv', names=['sales', 'date', 'region'])
df.sort_values('date', inplace=True)

app = Dash(__name__)

radio_values = ["all"] + list(df.region.unique())

chart_title = html.H1(children='Pink Morsel Sales', style={'textAlign':'center'})
chart_radios = dcc.RadioItems(radio_values, "all", id="region", inline=True, style={
    'textAlign':'center',
    'display': 'flex', 'gap': '20px',
    'alignItems': 'center', 'justifyContent': 'center',
    'fontFamily': 'sans-serif'})

chart = dcc.Graph(id='graph-content')

app.layout = html.Div([
    html.Header(children=[chart_title]),
    html.Main(children=[
        html.Section(children=[
            chart_radios
        ]),
        html.Div([chart])
    ])
])

@callback(
    Output('graph-content', 'figure'),
    Input('region', 'value')
)

def update_graph(value):
    dff = df[df.region == value] if value != "all" else df
    return px.line(dff, x='date', y='sales')

if __name__ == '__main__':
    app.run(debug=True)