import random
while True:
    number =int(input("enter number:"))
    a=(random.randint(1,5))
    print(a)
    if number==a:
        print("You win ")
        break
    else:
        print("wrong try again")
