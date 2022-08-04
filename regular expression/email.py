import re
pattern=r"[a-z0-9a-z]"
a=input("enter the number")
b=re.findall(pattern,a)
print(b)
