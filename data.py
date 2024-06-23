import pandas as pd

df = pd.read_csv('weather_dataset.csv', sep=',')
all_cities = df['name'].unique()
all_datas = df['datetime'].unique()