# Create a new collection called "products" and insert documents with fields like "name", "price", and "category".
# Create an index on the "price" field.
# Write a query to find all products in a specific category with a price range between $10 and $50.


import pymongo
from pymongo import MongoClient
from datetime import datetime
from pprint import pprint

client = MongoClient('localhost',27017)
db = client['test']

products = db.products

catalogue = [{
    'name': 'Laptop',
    'price': 200,
    'category': 'Electronics'
},{
    'name': 'Screen guard',
    'price': 30,
    'category': 'Accessories'
},{
    'name': 'Charging Cable',
    'price': 20,
    'category': 'Accessories'
}]

# products.insert_many(catalogue)

products.create_index([('price', pymongo.ASCENDING)])
for product in products.find({'price':{'$gt': 10, '$lt': 50}}):
    pprint(product)