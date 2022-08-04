class Student:
    def __init__(self,name,rollno,mark):
        self.name=name
        self.__rollno=rollno
        self._mark=mark
    def getRollno(self):
        return self.__rollno
    def setRollno(self,rollno):
        self.__rollno=rollno
a=Student("ruby","123","55")
print(a.getRollno())
a.setRollno(1222)
print(a.setRollno())
