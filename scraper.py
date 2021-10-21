import pandas as pd
import re


def getjson():
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'
    raw_data = pd.read_csv(url)

    time = raw_data['time']
    lat = raw_data['latitude']
    lon = raw_data['longitude']
    depth = raw_data['depth']
    mag = raw_data['mag']

    zone, place = [], []
    for row in raw_data['place']:
        x = re.split(',', row)
        zone.append(x[0])
        place.append(x[-1])

    final_data = pd.DataFrame(
        {
            "time": time,
            "latitude": lat,
            "longitude": lon,
            "depth": depth,
            "magnitude": mag,
            "zone": zone,
            "place": place
        }
    )

    mongo_docs = []
    for _, row in final_data.iterrows():
        feature = {'type': 'Feature',
                   'properties': {},
                   'geometry': {'type': 'Point',
                                'coordinates': []}}
        feature['geometry']['coordinates'] = [row['longitude'], row['latitude']]
        for prop in final_data.columns:
            feature['properties'][prop] = row[prop]
        mongo_docs.append(feature)
    return mongo_docs
