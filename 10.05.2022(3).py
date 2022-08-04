a={1:11,2:15}
b={4:13,5:25}
c={}
for i in (a,b,c):
    c.update(i)
print(c)
