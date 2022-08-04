import pymongo
connection=pymongo.MongoClient("mongodb://localhost:27017")
mydb=connection["Logindatabase"]
mycol=mydb["email and password"]
data=[{"name":"vimal","phoneNo":"8681080186","email":"vimal@gmail.com","password":"2313"},{"name":"ruby","phoneNo":"6369759661","email":"ruby@gmail.com","password":"1323"},{"name":"mouna","phoneNo":"9942548788","email":"mouna@gmail.com","password":"0000"}]
mycol.insert_many(data)
while(True):
    a=input("Login page \n Register \n Login")
    if(a=="Login" or a=="login"):
        email=input("email:")
        password=input("password:")
        x=mycol.find()
        for data in x:
            if(data["email"]==email and data["password"]==password):
                print("Login successfully")
                break
        else:
            print("incorrect password please try again")
        break
    

