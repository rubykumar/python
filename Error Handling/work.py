try:
    a=int(input("Enter the number:"))
    if(a%3==0):
        raise ValueError
    else:
        print(a,"is not divisible by 3")
except:
    print(a,"is divisible by 3")
