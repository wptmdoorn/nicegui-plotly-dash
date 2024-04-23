import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px

import flask
import pandas as pd
import os


def page(requests_pathname_prefix: str = None):
    server = flask.Flask(__name__)
    server.secret_key = os.environ.get('secret_key', 'secret')

    df = pd.read_csv(
        'https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

    app = dash.Dash(__name__, server=server,
                    requests_pathname_prefix=requests_pathname_prefix)

    app.layout = html.Div([
        html.H1(children='Dash App', style={'textAlign': 'center'}),
        dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
        dcc.Graph(id='graph-content')
    ])

    @callback(
        Output('graph-content', 'figure'),
        Input('dropdown-selection', 'value')
    )
    def update_graph(value):
        dff = df[df.country == value]
        return px.line(dff, x='year', y='pop')

    return app
