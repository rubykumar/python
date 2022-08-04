class Phone:
    def __init__(self,name,price,brand):
        self.name=name
        self.price=price
        self.brand=brand
    def makecall(self):
        print("you can make a call")
    def ringing(self):
        print("hello")
class Mobile(Phone):
    def __init__(self,name,price,brand,battery):
        self.name=name
        self.price=price
        self.brand=brand
        self.battery=battery
    def  gaming(self):
        print("playing ludo game")
    def calculator(self):
        print("perform basic calculator")
    def messaging(self):
        print("send and receive messsage")
class SmartPhone(Mobile):
    nokia=Mobile("nokia",3500,"v1",3500)
    nokia.makecall()
    nokia.ringing()
    nokia.gaming()
    nokia.calculator()
    nokia.messaging()
