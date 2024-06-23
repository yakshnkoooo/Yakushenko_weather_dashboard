from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from data import df, all_cities, all_datas

layout = dbc.Container([
    dbc.Row ([
        dbc.Col(
             html.Div([
                html.H1("Температура в городах Москва, Санкт-Петербург и Калининград"),
                html.P("Используйте фильтры выбора города и даты, чтобы увидеть результат."),
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
                value = all_cities[0],
                multi = False
            ),
        ]),
      
        dbc.Col([
            dbc.Label("Выберите дату:"),
            dcc.DatePickerSingle(
                id='crossfilter-datas',
                min_date_allowed=all_datas[0],
                max_date_allowed=all_datas[-1],
                initial_visible_month=all_datas[0],
                date=all_datas[0],
            ),
        ]),
    ]),

    dbc.Row([
        dbc.Col([
            html.P(id='avg_temp'),
            html.P(id='max_temp'),
            html.P(id='min_temp'),
            html.P(id='feels'),
        ], style={'textAlign': 'center', 'font-size': '36px', 'margin-top': '130px'}),

        dbc.Col([
            dbc.Card([
                dbc.Row(id='image')
            ])
        ])
    ])
])

@callback(
    Output('avg_temp', 'children'),
    Output('max_temp', 'children'),
    Output('min_temp', 'children'),
    Output('feels', 'children'),
    Input('crossfilter-cities', 'value'),
    Input('crossfilter-datas', 'date')
)
def update_info(city, data):
    day = pd.DataFrame(df[(df['datetime'] == data) & (df['name'] == city)]).reset_index()
    avg_temp ="Средняя температура: " + str(day['temp'][0]) +"C"
    max_temp = "Максимальная температура: " + str(day['tempmax'][0]) + "C"
    min_temp = "Минимальная температура: " + str(day['tempmin'][0]) + "C"
    feels = "Ощущается как: " + str(day['feelslike'][0]) + "C"
    return avg_temp, max_temp, min_temp, feels

@callback(
    Output('image', 'children'),
    Input('crossfilter-cities', 'value')
)
def update_card_image(city):
    if city == 'Moscow':
        card_image = dbc.CardImg(src='/static/images/moscow.png')
    elif city == 'St. Petersburg':
        card_image = dbc.CardImg(src='/static/images/saint_petersburg.png')
    else:
        card_image = dbc.CardImg(src='/static/images/kaliningrad.png')
    return card_image