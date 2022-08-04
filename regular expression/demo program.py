import re
##a=int(input("Enter the string"))
##if(a>11):
##    print(a)
##else:
##    print("You entered number is wrong")
pattern=r"\b\w{4}\b"
a=input("Enter the string")
b=re.findall(pattern,a)
print(b)
