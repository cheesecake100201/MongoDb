import pymongo
from pymongo import MongoClient
from bson.json_util import dumps

pipeline = [{
    "$match":{"operationType":"insert"}
}]

client = MongoClient('localhost',27017)
db = client['test']
employees = db.employees

change_stream = employees.watch(pipeline=pipeline)

for change in change_stream:
    new_document = change['fullDocument']
    print(f"New document inserted: {dumps(new_document)}")