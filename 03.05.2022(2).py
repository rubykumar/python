##i=14321
##while(i==14321):
##    print(14321%10)
##    i+=1
##    print()
####    if(i<=i[-2]):
####       print(1432%10)
######    print()
##i=14321
##while(i==14322):
##    print(i)
##else:
##    i.reverse(i)
##    print(i)
num=int(input("Enter the number:"))
reverse=0
while(num!=0):
    a=num%10
    reverse=(reverse*10)+a
    num//=10
print("reverse:"+str(reverse))
