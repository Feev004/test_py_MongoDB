from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['MyDB']
td = db['myCollection_customers']
# delete_result = td.delete_many({"age": 35})
# td.delete_one({}) 
# delete_result =td.delete_many({"id": 1})
# delete_result =td.delete_many({"id": 2})
# delete_result =td.delete_many({"id": 3})
# delete_result =td.delete_many({"id": 4})
# delete_result =td.delete_many({"id": 5})
num = 0
for customer in td.find():
    num += 1
print(num)
for i in range(1, num+1):
    delete_result = td.delete_many({"id": i})

print(f"Deleted {delete_result.deleted_count} documents")