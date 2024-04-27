from dash import html
import dash_bootstrap_components as dbc

variableA = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('LOGO', style={'font-size': '36px'}), md=16, style={'background-color': 'red'}),
        dbc.Col(html.H1('DISEÑA TU CANAL', style={'font-size': '36px'}), md=14, style={'background-color': 'skyblue'}, align="center"),
    ])
])