import pymongo as mongo
from scraper import getjson

data = getjson()
print("Function Working Properly")

try:
    connection = mongo.MongoClient('mongodb://localhost:27017/')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = connection["USGS"]
Collection = db["testing"]

if isinstance(data, list):
    Collection.drop()
    Collection.insert_many(data)
else:
    Collection.drop()
    Collection.insert_one(data)
