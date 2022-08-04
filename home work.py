n=int(input("Enter the pattern="))
val=n*2-1
for i in range (1,val+1):
    for j in range(1,val+1):
        if(i==j or j==val-i+1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
