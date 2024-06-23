from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from data import df, all_cities, all_datas

layout = dbc.Container([
    dbc.Row ([
        dbc.Col(
             html.Div([
                html.H1("Дашборд прогноза погоды"),
                html.P("Проект выполнен студентами группы БСБО-13-21 Вучетичем Георгием и Якушенко Иваном"),
                html.Hr(style={'color': 'black'}),
            ], style={'textAlign': 'center'}), 
        )
    ]),

    html.Br(),

    dbc.Row([
        html.P("В основе дашборда лежит датасет с данными о погоде в городах Москва, Санкт-Петербург и Калининград в период 01.04.2024-31.02.2024."),
        html.P("Дашборд содержит такие страницы, как температура погоды в городе сейчас; температура в городе в определенный день из архивного датасета; сравнение температур в городах за архивный период; статистика погодных условий по всем трем городам за архивный период."),
        html.P("Ссылка на вебсайт с проектом: http://yakushenko.pythonanywhere.com/"),
        html.P("Ссылка на проект в GitHub: https://github.com/yakshnkoooo/Yakushenko_weather_dashboard")
    ])
])