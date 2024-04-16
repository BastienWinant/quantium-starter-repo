from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('processed_data.csv', names=['sales', 'date', 'region'])
df.sort_values('date', inplace=True)

colors = {
    "chart_background": "#e5e5e5",
    "chart_line": "#e5e5e5",
    "chart_text": "#14213d",

}
app = Dash(__name__)

radio_values = ["all"] + list(df.region.unique())

title_style = {
    'background': '#000000',
    'color': '#FFFFFF',
    'fontFamily': 'sans-serif',
    'fontWeight': 'bold',
    'textAlign': 'center'
}
chart_title = html.H1(children='Pink Morsel Sales')

chart_radios = dcc.RadioItems(radio_values, "all", id="region", inline=True, style={
    'textAlign':'center', 'textTransform': 'capitalize',
    'display': 'flex', 'gap': '20px',
    'alignItems': 'center', 'justifyContent': 'center',
    'fontFamily': 'sans-serif'})

chart = dcc.Graph(id='graph-content')

app.layout = html.Div([
    html.Header(children=[chart_title], style=title_style),
    html.Main(children=[
        html.Section(children=[
            chart_radios
        ]),
        html.Div([chart])
    ], style={
        'backgroundColor': "#e5e5e5"
    })
])

@callback(
    Output('graph-content', 'figure'),
    Input('region', 'value')
)

def update_graph(value):
    dff = df[df.region == value] if value != "all" else df
    fig = px.line(dff, x='date', y='sales')

    fig.update_layout(
        font = {
            'color': colors['chart_text'],
            'size': 14
        },
        margin={
            "t": 100,
            "b": 100,
            "r": 100,
            "l": 100
        },
        plot_bgcolor=colors['chart_background'],
        paper_bgcolor=colors['chart_background'],
        colorway=["#8c564b"]
)
    return fig

if __name__ == '__main__':
    app.run(debug=True)