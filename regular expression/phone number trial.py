import re
pattern=r"^[6789]\d{9}$"
a=input("Enter the number")
b=re.search(pattern,a)
if(b):
    print("Match Found")
else:
    print("Match not found")
