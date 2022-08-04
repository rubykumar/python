##n=int(input("Enter the rows:"))
alphabet=64
for i in range(1,15):
    for j in range(1,15-i+1):
        print(j,end=" ")
    for k in range(i,0,-1):
        print("%c" %(alphabet+k),end=" ")
##    for l in range(2,i+1):
##        print("%c" %(alphabet+l),end=" ")
    print()
