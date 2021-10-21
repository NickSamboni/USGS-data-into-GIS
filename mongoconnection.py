import pymongo as mongo
from scraper import getdata

#getting the returned object from the function that constructs the data 
data = getdata()
print("Function Working Properly")

#connecting to mongodb local database
try:
    connection = mongo.MongoClient('mongodb://localhost:27017/')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

#these are the credentials for the specific database and collection of choise
db = connection["USGS"]
Collection = db["testing"]

#checking for the structure of the object returned from getdata()
if isinstance(data, list):
    #Collection.drop()
    Collection.insert_many(data)
else:
    Collection.drop()
    Collection.insert_one(data)
