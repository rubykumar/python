val=int(input("Enter any value:"))
print("Result of a given",val,"are:")
for i in range(1,val):
    if(val%i==0):
        print(i)
