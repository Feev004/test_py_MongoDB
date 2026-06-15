from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['MyDB']
td = db['myCollection_customers']
num = 0
for customer in td.find():
    num += 1
    print(num, customer["name"], customer["age"])
    # print(customer)