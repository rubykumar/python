class company:
    def __init__(self,name,dept,place):
        self.name=name
        self.dept=dept
        self.place=place
    def Salaryamount(self):
        print("Your salary amount is 10000")
class Mnc(company):
    def __init__(self,name,dept,place,product):
        super().__init__(name,dept,place)
        self.product=product
    def salaryamount(self):
        print("Your salary amount is 2000000")
a=Mnc("ruby","QC","villianur","Tablets")
a.salaryamount()
