import pymongo
a=pymongo.MongoClient("mongodb://localhost:27017")
mydb=a["database"]
mycol=mydb["mark list"]
print(mycol)
data=[{"name":"jo","dept":"bsc","mark":98},{"name":"kavi","dept":"Bsc nursing","mark":95}]
for i in mycol.find():
    print(i)