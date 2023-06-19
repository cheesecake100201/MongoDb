import pymongo
import datetime
from pprint import pprint
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['test']

articles = db.articles

articles_data = [
    {
        'title': 'Introduction to MongoDB',
        'content': 'MongoDB is a NoSQL database...',
    },
    {
        'title': 'Python Programming Guide',
        'content': 'Python is a powerful programming language...',
    },
    {
        'title': 'Web Development Basics',
        'content': 'Web development involves creating...',
    }
]

# articles.insert_many([articles_data])

articles.create_index([('content', pymongo.TEXT)])

for article in articles.find({"$text":{"$search":"python"}}):
    pprint(article)