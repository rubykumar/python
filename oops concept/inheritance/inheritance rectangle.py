class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def get_area(self):
        return (self.length*self.breadth)
class Cuboid(Rectangle):
    def __init__(self,length,breadth,height):
        super().__init__(length,breadth)
        self.height=height
    def get_cuboid(self):
        return(super().get_area()*self.height)
r=Cuboid(2,3,4)
print(r.get_area())
print(r.get_cuboid())
