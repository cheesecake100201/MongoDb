# Given a collection of documents representing students, each containing fields like "name", "age", and "grade", 
# write a MongoDB query to calculate the average age and average grade for each grade level.


import pymongo
from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost',27017)

db = client['test']

students = db.students

students_data = [
    {
        "name": "Alice",
        "age": 20,
        "grade": "A"
    },
    {
        "name": "Bob",
        "age": 22,
        "grade": "B"
    },
    {
        "name": "Charlie",
        "age": 21,
        "grade": "C"
    },
    {
        "name": "David",
        "age": 23,
        "grade": "A"
    },
    {
        "name": "Eva",
        "age": 24,
        "grade": "B"
    },
    {
        "name": "Frank",
        "age": 22,
        "grade": "A"
    },
    {
        "name": "Grace",
        "age": 21,
        "grade": "C"
    },
    {
        "name": "Henry",
        "age": 20,
        "grade": "B"
    },
    {
        "name": "Ivy",
        "age": 19,
        "grade": "A"
    },
    {
        "name": "Jack",
        "age": 18,
        "grade": "C"
    }
]

students.insert_many(students_data)

query = [{
    "$group":{"_id":"$grade",
              "average_age":{"$avg":"$age"},
              "count":{"$sum":1}}
},{
    "$sort":{"_id":1}
}]

for student in students.aggregate(query):
    pprint(student)