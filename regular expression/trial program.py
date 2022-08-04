import re
pattern=r"\b\d{2,4}\b"
a="i am recently used this 95 146 855 4956, number but 3524654,this my old number currently i am using 541456144 number"
b=re.findall(pattern,a)
print(b)
