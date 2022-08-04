class Rectangle:
    def __init__(self,a,b):
        self.length=a
        self.breadth=b
    def get_Area(self):
        print("Area of the rectangle is",self.length*self.breadth)
    def get_Perimeter(self):
        print("Perimeter of the rectangle is ",2*(self.length+self.breadth))
r=Rectangle(3,3)
r.get_Area()
r.get_Perimeter()
