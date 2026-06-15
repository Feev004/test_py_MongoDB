from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['MyDB']
td = db['myCollection_customers']

td.update_one({"id": 1}, {"$set": {"name": "John see"}})
print("Data updated successfully")