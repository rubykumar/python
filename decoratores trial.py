def outer (func):
    def inner (a,b):
        if(b!=0):
            func (a,b)
        else:
            print(0)
    return inner

a=inner(2,2)
print(a)
