##try:
##    a=int(input("enter a number"))
##    b=int(input("enter a number"))
##    c=a//b
##except Exception as a:
##    print("error",a)
##else:
##    print("no error")
##finally:
##    print("finally block executed")
try:
    a=int(input("enter a number"))
    if(a>10000):
        raise ValueError
    else:
        print("you can withdraw amount",a)
except:
    print("only withdraw amount less than 10000")
