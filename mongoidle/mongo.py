import pymongo
connection=pymongo.MongoClient("mongodb://localhost:27017")
mydb=connection["mydatabase"]
mycol=mydb["customers"]
data=[{"name":"vimal","age":29,"place":"Ariyanguppam"},{"name":"mouna","age":1,"place":"Ariyanguppam"}]
myquery={"place":"Villianur"}
a=mycol.find(myquery)
for myquery in a:
    print(myquery)
