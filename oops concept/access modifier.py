class company:
    def __init__(self,cname,place,salary):
        self.cname=cname
        self._place=place
        self.__salary=salary
    def companyname(self):
        print(self.cname)
    def salary(self):
        print("Enter the employee salary",self.__salary)
a=company("sterilgene","Puducherry",5000)
print(a._place)
a.salary()
a.companyname()
