import pandas as pd
import requests
import re
from geojson import FeatureCollection, Feature, Point
import json

def getjson():
    print ('Starting...')
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'
    raw_data = pd.read_csv(url)
    print ('url fetch correctly')

    time = raw_data['time']
    lat =  raw_data['latitude']
    lon =  raw_data['longitude']
    depth = raw_data['depth']
    mag =  raw_data['mag']

    zone, place = [], []
    for row in raw_data['place']:
        x=re.split(',',row)
        zone.append(x[0])
        place.append(x[-1])

    final_data = pd.DataFrame(
        {
            "time":time,
            "latitude":lat,
            "longitude":lon,
            "depth":depth,
            "magnitude":mag,
            "zone":zone,
            "place":place
        }
    )
    #final_data.to_json('datamongo.json',orient="records")

    points = []
    features = final_data.apply(lambda row: points.append( (float(row["longitude"]), float(row["latitude"]))), axis=1).tolist()
    properties = final_data.drop(['latitude', 'longitude'], axis=1).to_dict('records')
    feature_collection = FeatureCollection(features=features, properties=properties)
    with open('data.geojson', 'w', encoding='utf-8') as f:
        json.dump(feature_collection, f, ensure_ascii=False)

getjson()
