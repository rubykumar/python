def Number(n):
    if(n>0):
        return n*Number(n-1)
    else:
        return 1  
print(Number(5))

##5*Number(5-1)4
##5*4*Number(4-1)3
##5*4*3*Number(3-1)2
##5*4*3*2*Number(2-1)1
##5*4*3*2*1*Number(1-1)0




