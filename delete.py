from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['MyDB']
td = db['myCollection_customers']
delete_result = td.delete_many({"age": 35})
print(f"Deleted {delete_result.deleted_count} documents with age 35")
# td.delete_one({}) 
# td.delete_many({"id": 1})
# td.delete_many({"id": 2})
# td.delete_many({"id": 3})
# td.delete_many({"id": 4})
# td.delete_many({"id": 5})

print("Data deleted successfully")