from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['MyDB']
td = db['myCollection_customers']

td.insert_one({
    "id":1,
    "name":"John Doe",
    "age":30,
})
td.insert_many([
    {
        "id":2,
        "name":"Jane Doe",
        "age":25,
    },
    {
        "id":3,
        "name":"Alice Smith",
        "age":28,
    },
    {
        "id":4,
        "name":"Bob Johnson",
        "age":35,
    },
    {
        "id":5,
        "name":"Bob Williams",
        "age":35,
    }
])
print("Data inserted successfully")