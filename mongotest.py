import pymongo
client= pymongo.MongoClient("mongodb+srv://Ritika:123456R@cluster0.x0tbdmp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test
print(db)

d={ "name":"ritika",
    "email" : "ritika@gmail.com",
    "surname": "gupta"}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
# coll is collection .it is simply a variable.
#client is just a connection.