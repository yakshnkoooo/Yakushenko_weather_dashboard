from dash import html, dcc, callback, Output, Input
import pandas as pd
from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from datetime import date

from data import df
red = '#d5e486'
green = '#eab748'
blue = '#b876e5'

layout = dbc.Container([
    dbc.Row ([
        dbc.Col(
            html.Div([
                html.H1("Статистика погодных условий по городам Москва, Санкт-Петербург и Калининград"),
                html.P("Используйте фильтр выбора диапазона дат, чтобы увидеть результат."),
                html.Hr(style={'color': 'black'}),
            ], style={'textAlign': 'center'}), 
        )
    ]),

    html.Br(),

    html.Div(
        dcc.DatePickerRange(
            id='range',
            min_date_allowed=date(2023,4,1),
            max_date_allowed=date(2024,1,31),
            start_date=date(2023,4,1),
            end_date=date(2024,1,31),
            style={'textAlign':'center'}
        ), style={'textAlign':'center'}
    ),
    dbc.Row([
        dbc.Col([
            dbc.Row(dcc.Graph(id='sunny', config={'displayModeBar':False})),
            dbc.Row(html.P(id='sunny_text_M', style={'background-color':green, 'textAlign':'center'})),
            dbc.Row(html.P(id='sunny_text_S', style={'background-color':blue, 'color':'#ffffff', 'textAlign':'center'})),
            dbc.Row(html.P(id='sunny_text_K', style={'background-color':red, 'textAlign':'center'}))
        ]),
        dbc.Col([
            dbc.Row(dcc.Graph(id='rainy', config={'displayModeBar':False})),
            dbc.Row(html.P(id='rainy_text_M', style={'background-color':green, 'textAlign':'center'})),
            dbc.Row(html.P(id='rainy_text_S', style={'background-color':blue, 'color':'#ffffff', 'textAlign':'center'})),
            dbc.Row(html.P(id='rainy_text_K', style={'background-color':red, 'textAlign':'center'}))
        ]),
        dbc.Col([
            dbc.Row(dcc.Graph(id='snowy', config={'displayModeBar':False})),
            dbc.Row(html.P(id='snowy_text_M', style={'background-color':green, 'textAlign':'center'})),
            dbc.Row(html.P(id='snowy_text_S', style={'background-color':blue, 'color':'#ffffff', 'textAlign':'center'})),
            dbc.Row(html.P(id='snowy_text_K', style={'background-color':red, 'textAlign':'center'}))
        ]),
    ])
])
@callback(
    [Output('sunny','figure'),
     Output('sunny_text_M','children'),
     Output('sunny_text_S','children'),
     Output('sunny_text_K','children'),
     Output('rainy','figure'),
     Output('rainy_text_M','children'),
     Output('rainy_text_S','children'),
     Output('rainy_text_K','children'),
     Output('snowy','figure'),
     Output('snowy_text_M','children'),
     Output('snowy_text_S','children'),
     Output('snowy_text_K','children')],
     Input('range','start_date'),
     Input('range','end_date')
)
def update_diagrams(start_date, end_date):
    df_sort = df[(df['datetime'] > start_date) & (df['datetime'] < end_date)]
    statistics = df_sort.groupby(by=['name','icon']).count()['temp'].reset_index().sort_values(by='icon')
    left = pd.Series(df["name"].unique())
    left.name = "name"
    right = pd.Series(df["icon"].unique())
    right.name = "icon"
    temp = pd.merge(left,right,how="cross")
    statistics = pd.merge(statistics,temp,how="right").fillna(0).sort_values(by=['icon','name']).reset_index()
    sunny=go.Figure(go.Pie(labels=statistics['name'].unique(), values=statistics['temp'][0:3], textinfo='label+percent', title={'text':'Процентное соотношение солнечных дней','position':'bottom center'}, marker={'colors':[red,green,blue]}))
    sunny.update_layout(showlegend=False)
    sunny_text_M="Москва: " + str(int(statistics['temp'][1]))
    sunny_text_S="Санкт-Петербург: " + str(int(statistics['temp'][2]))
    sunny_text_K="Калининград: " + str(int(statistics['temp'][0]))
    rainy=go.Figure(go.Pie(labels=statistics['name'].unique(), values=statistics['temp'][9:12], textinfo='label+percent', title={'text':'Процентное соотношение дождливых дней','position':'bottom center'}, marker={'colors':[red,green,blue]}))
    rainy.update_layout(showlegend=False)
    rainy_text_M="Москва: " + str(int(statistics['temp'][10]))
    rainy_text_S="Санкт-Петербург: " + str(int(statistics['temp'][11]))
    rainy_text_K="Калининград: " + str(int(statistics['temp'][9]))
    snowy=go.Figure(go.Pie(labels=statistics['name'].unique(), values=statistics['temp'][12:15], textinfo='label+percent', title={'text':'Процентное соотношение снежных дней','position':'bottom center'}, marker={'colors':[red,green,blue]}))
    snowy.update_layout(showlegend=False)
    snowy_text_M="Москва: " + str(int(statistics['temp'][13]))
    snowy_text_S="Санкт-Петербург: " + str(int(statistics['temp'][14]))
    snowy_text_K="Калининград: " + str(int(statistics['temp'][12]))
    return sunny,sunny_text_M,sunny_text_S,sunny_text_K,rainy,rainy_text_M,rainy_text_S,rainy_text_K,snowy,snowy_text_M,snowy_text_S,snowy_text_K