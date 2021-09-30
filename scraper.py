import pandas as pd
import requests
import re

def scrapper():
    print ('Starting...')
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'
    raw_data = pd.read_csv(url)
    print ('url fetch correctly')

    time = raw_data['time']
    lat =  raw_data['latitude']
    lon =  raw_data['longitude']
    depth = raw_data['depth']
    mag =  raw_data['mag']
    geocode =  raw_data['place']

    place = []
    for row in raw_data['place']:
        x=re.split(',',row)
        place.append(x[-1])

    final_data = pd.DataFrame(
        {
            "time":time,
            "latitude":lat,
            "longitude":lon,
            "depth":depth,
            "magnitude":mag,
            "geocode":geocode,
            "state/country":place
        }
    )
    print(final_data)

scrapper()

