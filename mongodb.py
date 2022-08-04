import pymongo 
connection=pymongo.MongoClient("mongodb://localhost:27017")
print("connection created")
mydb=connection["Student database"]
mycol=mydb["Student account creation"]
data={"name":"vimal","age":28,"dept":"B.com"}
x=mycol.insert_one(data)
print(x.inserted_id)