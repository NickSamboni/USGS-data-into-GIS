import pymongo as mongo
from scraper import getjson
import json

getjson()
print("Function Working Properly")

try:
    connection = mongo.MongoClient('mongodb://localhost:27017/')
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")

db = connection["USGS"]
Collection = db["testing"]

with open('data.geojson') as file:
    file_data = json.load(file)

if isinstance(file_data, list):
    Collection.insert_many(file_data)  
else:
    Collection.insert_one(file_data)


