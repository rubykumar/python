class Person:
    def __init__(self,firstname,lastname,age):
        self.__firstname=firstname
        self.__lastname=lastname
        self.__age=age
    def setFirstname(self):
        print("Your first name is",self.__firstname)
    def setLastname(self):
        print("Your last name is",self.__lastname)
    def setage(self,a):
        if (a>0 and a<=100):
            print(self.__age)
        else:
            print(0)
a=Person("ruby","jo",18)
a.setFirstname()
a.setage(10000)
            
