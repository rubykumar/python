a=int(input("Enter the length of the list:"))
lst=[]
b=[]
for i in range(a):
    x=int(input("Enter element"))
    lst.append(x)
print(lst)
b=lst[-1:-(len(lst)+1):-1]
print(b)
    
    
        
