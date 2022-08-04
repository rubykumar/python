a=int(input("Enter the a value: "))
b=int(input("Enter the b value: "))
c=int(input("Enter the c value: "))
if(a>b and a>c):
    print("a is greater")
    if(b<c):
        print("b is smaller")
    else:
        print("c is smaller")
elif(b>c and b>a):
    print("b is greater")
    if(a<c):
        print("a is smaller")
    else:
        print("c is smaller")
else:
    print("c is greater")
    if(a<b):
        print("a is smaller")
    else:
        print("b is smaller")
