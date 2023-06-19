import pymongo
from pprint import pprint
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['test']

restaurants = db.restaurants

restaurants_data = [
    {
        'name': 'Restaurant A',
        'location': {
            'type': 'Point',
            'coordinates': [40, 69]
        },
        'cuisine': 'Italian'
    },
    {
        'name': 'Restaurant B',
        'location': {
            'type': 'Point',
            'coordinates': [8, 42]
        },
        'cuisine': 'Mexican'
    },
    {
        'name': 'Restaurant C',
        'location': {
            'type': 'Point',
            'coordinates': [90,88]
        },
        'cuisine': 'Chinese'
    }
]

# restaurants.insert_many(restaurants_data)

restaurants.create_index([('location',pymongo.GEOSPHERE)])

query = {'location':{'$near':{'$geometry':{'type':'Point','coordinates':[8,42]}, '$maxDistance':5000}}}
for restaurant in restaurants.find(query):
    pprint(restaurant)