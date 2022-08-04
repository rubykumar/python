import pymongo
connection=pymongo.MongoClient("mongodb://localhost:27017")
mydb=connection["mydatabase"]
mycol=mydb["name list"]
data=[{"name":"vimal","age":29,"dept":"B.com"},{"name":"ruby","age":22,"dept":"Bsc"}]
x=mycol.insert_many(data)
print(x.inserted_ids)