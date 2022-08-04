import functools
a=[-1,2,3,-8,-5]
def add(x,y):
    return x+y
c=functools.reduce(add,a)
print(c)

import functools
a=[-1,2,3,-8,-5]
def sub(x,y):
    return x-y
c=lambda(functools.reduce(sub,a))
##c=lambda(functoool.reduce(add,a))
print(c)
