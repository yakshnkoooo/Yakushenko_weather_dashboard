from dash import html, dcc, callback, Output, Input
import pandas as pd
from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from datetime import date
import plotly.express as px

from data import df, all_cities, all_datas

layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div([
                html.H1("Сравнение температур в городах Москва, Санкт-Петербург и Калининград"),
                html.P("Используйте фильтры выбора города и диапазона дат, чтобы увидеть результат."),
                html.Hr(style={'color': 'black'}),
            ], style={'textAlign': 'center'}), 
        )
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dbc.Label("Выберите город:"),
            dcc.Dropdown(
                id = 'crossfilter-cities',
                options = [{'label': i, 'value': i} for i in all_cities],
                value = all_cities[0:2],
                multi = True
            ),
        ]),
      
        dbc.Col([
            dbc.Label("Выберите дату:"),
            dcc.DatePickerRange(
                id='crossfilter-datas',
                min_date_allowed=all_datas[0],
                max_date_allowed=all_datas[-1],
                start_date=date(2023, 4, 1),
                end_date=date(2023, 4, 10),
            ),
        ]),
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='line')
        ]),

        dbc.Col([
            dcc.Graph(id='bar')
        ])
    ])
])

@callback(
    Output('line', 'figure'),
    Input('crossfilter-cities', 'value'),
    Input('crossfilter-datas', 'start_date'),
    Input('crossfilter-datas', 'end_date')
)
def update_line(city, sdate, edate):
    filtered_data = df[(df['name'].isin(city)) & (df['datetime'] > sdate) & (df['datetime'] < edate)]
    figure = px.line(
        filtered_data,
        x = 'datetime',
        y = 'temp',
        color = 'name',
        color_discrete_map = {'Moscow': '#eab748', 'St. Petersburg': '#b876e5', 'Kaliningrad': '#d5e486'},
        labels={'datetime':'Дата', 'temp': 'Температура'},
        markers = True,
    )
    return figure

@callback(
    Output('bar', 'figure'),
    Input('crossfilter-cities', 'value'),
    Input('crossfilter-datas', 'start_date'),
    Input('crossfilter-datas', 'end_date')
)
def update_bar(city, sdate, edate):
    filtered_data = df[(df['name'].isin(city)) & (df['datetime'] > sdate) & (df['datetime'] < edate)]
    figure = px.bar(
        filtered_data,
        x = 'datetime',
        y = 'temp',
        color = 'name',
        color_discrete_map = {'Moscow': '#eab748', 'St. Petersburg': '#b876e5', 'Kaliningrad': '#d5e486'},
        labels={'datetime':'Дата', 'temp': 'Температура'},
        barmode = 'group'
    )
    return figure