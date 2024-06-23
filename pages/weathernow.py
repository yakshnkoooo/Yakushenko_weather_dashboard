from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import requests
from data import df, all_cities, all_datas

layout = dbc.Container([
    dbc.Row ([
        dbc.Col(
             html.Div([
                html.H1("Температура сейчас в городах Москва, Санкт-Петербург и Калининград"),
                html.P("Используйте фильтр выбора города, чтобы увидеть результат."),
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
            )
        ]),

        dbc.Col([
            
        ])
    ]),

    dbc.Row([
        dbc.Col([
            html.P(id='temp_now'),
        ], style={'textAlign': 'center', 'font-size': '36px', 'margin-top': '240px'}),

        dbc.Col([
            dbc.Card([
                dbc.Row(id='image1')
            ])
        ])
    ])
])

@callback(
    Output('temp_now', 'children'),
    Input('crossfilter-cities', 'value')
)
def update_info(city):
    if city == 'Moscow':
        m = 'Москва'
        url1 = 'https://api.openweathermap.org/data/2.5/weather?q='+m+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
        weather_data1 = requests.get(url1).json()
        temperature1 = round(weather_data1['main']['temp'])
        t = "Температура сейчас: " + str(temperature1) + "C"
    elif city == 'St. Petersburg':
        s = 'Санкт-Петербург'
        url2 = 'https://api.openweathermap.org/data/2.5/weather?q='+s+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
        weather_data2 = requests.get(url2).json()
        temperature2 = round(weather_data2['main']['temp'])
        t = "Температура сейчас: " + str(temperature2) + "C"
    else:
        k = 'Калининград'
        url3 = 'https://api.openweathermap.org/data/2.5/weather?q='+k+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
        weather_data3 = requests.get(url3).json()
        temperature3 = round(weather_data3['main']['temp'])
        t = "Температура сейчас: " + str(temperature3) + "C"
    return t

@callback(
    Output('image1', 'children'),
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