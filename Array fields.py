import pymongo
from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)

db = client['test']

employees = db.employees

employees_data = [{
    "name": "Alice",
    "skills": ["Python", "Django", "JavaScript"]
  },
  {
    "name": "Bob",
    "skills": ["JavaScript", "React", "Node.js"]
  },
  {
    "name": "Carol",
    "skills": ["Java", "Spring", "Hibernate"]
  },
  {
    "name": "David",
    "skills": ["C#", "ASP.NET", "Azure"]
  },
  {
    "name": "Eve",
    "skills": ["Ruby", "Rails", "PostgreSQL"]
  },
  {
    "name": "Frank",
    "skills": ["Python", "Flask", "JavaScript"]
  },
  {
    "name": "Grace",
    "skills": ["JavaScript", "Angular", "Node.js"]
  },
  {
    "name": "Hannah",
    "skills": ["Java", "Spring Boot", "Hibernate"]
  },
  {
    "name": "Ivan",
    "skills": ["C#", "ASP.NET Core", "Azure"]
  },
  {
    "name": "Julia",
    "skills": ["Ruby", "Sinatra", "PostgreSQL"]
  }]

# employees.insert_many(employees_data)

query = {
    "skills":{"$in":["JavaScript"]}
}
for employee in employees.find(query):
    pprint(employee)