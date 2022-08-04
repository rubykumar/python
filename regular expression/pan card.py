import re
pattern=r"\b^[A-Z][A-Z]{2}[P][R]\d{4}[A-Z]$\b"
a=input("Enter the pan card number")
b=re.findall(pattern,a)
if(b):
    print("match found")
else:
    print("Wrong pattern please try again")
