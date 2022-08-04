import re
pattern=r"\b\D{2,4}\b"
string="Hi ruby from chennai 22 555"
b=re.findall(pattern,string)
print(b)
