import requests
from dotenv import load_dotenv,dotenv_values
import os
import base64
import datetime
import pandas as pd 

pd.set_option("display.max_columns", 500)
pd.set_option("display.max_rows", 500)

local = os.getcwd()
load_dotenv(local+r'\OpenWeather\.env')
geo_key = os.getenv('GEO_KEY')
lista = [] 
df = pd.read_csv(r"C:\Users\Caio\Documents\Courses\OpenWeather\weather.csv",header=0)

def get_location(city):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},&limit={5}&appid={geo_key}'
    response = requests.get(url)
    response2 = response.json()

    lat = response2[0]['lat']
    lon = response2[0]['lon']

    return lat, lon

def get_weather(lat,lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={geo_key}'
    response = requests.get(url)
    response2 = response.json()
    return response2

def append_csv_df(df):
    disc = {"name": current_weather['name'],
            "country": current_weather['sys']['country'], 
            "current weather": round(current_weather['main']['temp'],1),
            "feels like": round(current_weather['main']['feels_like'],1),
            "temp min": round(current_weather['main']['temp_min'],1),
            "temp max": round(current_weather['main']['temp_max'],1),
            "horario_extraido": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),}

    lista.append(disc)

    df_stage = pd.DataFrame(lista, index=[0],)
    df = pd.concat([df, df_stage], ignore_index=True)

    df.to_csv(r"C:\Users\Caio\Documents\Courses\OpenWeather/weather.csv", index=False,mode="w")

while True:
    insert_city = input("Do you want to insert a new city? (y/n): ")
    if insert_city.lower() == 'y':
        lati,long = get_location(input("Enter the city name: "))
        current_weather = get_weather(lati,long)
        append_csv_df(df)
        print("City added successfully!")
    elif insert_city.lower() == "n":
        print("No new city added.")
        print("The last city added was: ",df.iloc[-1]['name'])
        print(round(df.groupby('country').agg({'current weather': "mean"}).reset_index().sort_values(by='current weather', ascending=False),1))
        break
        # print(round(pd.pivot_table(data=df,values="current weather",index="country",aggfunc="mean"),1))
    elif insert_city.lower() != "n" and insert_city.lower() != "y":
        break