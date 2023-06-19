import pymongo
from pymongo import MongoClient
import pprint
from datetime import datetime, timedelta

client = MongoClient('localhost',27017)
db = client['test']
events = db.events

events_list = [{
    'event_name': 'Workshop',
    'event_date': datetime.now() + timedelta(days = 6)
},{
    'event_name': 'Conference',
    'event_date': datetime.now() + timedelta(days = 7)
},{
    'event_name': 'meetup',
    'event_date': datetime.now() + timedelta(days = 10)
}]

result = events.insert_many(events_list)
d = datetime.now() + timedelta(days=7)
for event in events.find({"event_date":{'$lte':d}}):
    pprint.pprint(event)


