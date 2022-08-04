##def vowel_count(Str):
##    vowel=0
##    constant=0
##    for i in Str:
##        if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U'):
##            vowel=vowel+1
##        else:
##            constant=constant+1
##    print("The number of vowel:",vowel)
##    print("The number of constant:",constant)
##vowel_count("Pythonlobby")

a=10
b=20
print(a)
def display():
    global a
    global b
    a=20
    b=10
    c=a*b
    print("inside the function")
    print(c)
display()
print("outside the function")
print(a)

