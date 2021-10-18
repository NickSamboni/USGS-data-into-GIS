import pymongo as mongo
from scraper import getjson
import json

data = getjson()
print(data)
print("Function Working Properly")

try:
    connection = mongo.MongoClient('mongodb://localhost:27017/')
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")

db = connection["USGS"]
Collection = db["testing"]

with open('datamongo.json') as file:
    file_data = json.load(file)

if isinstance('', list):
    Collection.drop()
    Collection.insert_many(getjson())
else:
    Collection.drop()
    Collection.insert_one(getjson())


