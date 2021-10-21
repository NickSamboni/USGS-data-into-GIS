import pandas as pd
import re


def getdata():
    #url that points to the csv file that contains all the data about earthquakes around the world
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'

    #using pandas to work with the dataframe
    raw_data = pd.read_csv(url)

    #create the objs that will work as columns for the final df
    time = raw_data['time']
    lat = raw_data['latitude']
    lon = raw_data['longitude']
    depth = raw_data['depth']
    mag = raw_data['mag']

    #forming the final df. Creating two new columns with the geo information.
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

    #Creating the geojson object neccesary to send data to mongodb as different documents
    #because it is needed to satisfy a specific structure
    mongo_docs = []
    for _, row in final_data.iterrows():
        feature = {'type': 'Feature',
                   'properties': {},
                   'geometry': {'type': 'Point',
                                'coordinates': []
                                }
                    }
        feature['geometry']['coordinates'] = [row['longitude'], row['latitude']]
        for prop in final_data.columns:
            feature['properties'][prop] = row[prop]
        mongo_docs.append(feature)

    #returning a list of dictionaries that contain the information for each seismic event
    return mongo_docs
