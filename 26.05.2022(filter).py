##a=[2,3,4,5,6]
##def add(a):
##     return(a%2==0)     
##b=filter(add,a)
##print(list(b))

##a=[2,3,4,5,6]
##b=filter(lambda a:a%2==0,a)
##print(list(b))

a=[1,2,3,4,5,6]
def odd(a):
    return(a%2!=0)
b=filter(odd,a)
print(list(b))

a=[1,2,3,4,5,6]
b=filter(lambda a:a%2==0,a)
print(list(b))
