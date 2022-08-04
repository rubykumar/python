n=int(input("Enter the number:"))
for i in range(n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for k in range(1,i+2):
        print(k, end= " ")
    print()
