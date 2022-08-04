import random
while True:
    number=int(input("Enter number:"))
    a=(random.randint(1,10))
    print(a)
    if(number==a):
        print("you win")
        break
    else:
        print("Wrong try again")                                                         
