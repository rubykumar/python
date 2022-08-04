class Dog:
    color="Black"
    age=4
    weight=12
    def bark(self):
        print("The dog is barking")
    def sleep(self):
        print("The dog is always sleeping")
    def eat(self):
        print("The dog is eat only biriyani")
jack=Dog()
print("jack  age is ",jack.age)
print("jack color is",jack.color)
jack.bark()
