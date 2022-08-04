import pymongo
connection=pymongo.MongoClient("mongodb://localhost:27017")
mydb=connection("mydatabase")
mycol=mydb("list")
data={"name":"dhivya","age":19,"dept":"biology"}
a=mycol.