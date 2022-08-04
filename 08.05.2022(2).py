a=int(input("Enter the numbers:"))
f=0
i=2
while i<=a/2:
    if a%i==0:
        f=1
        break
    i=i+1
    if f==0:
        print("The entered number is an prime number")
    else:
        print("The entered number not an prime number")
