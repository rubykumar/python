a={"Kumar","Vijaya","Kavi","Ruby","Jo"}
b={"mouna","vimal","Dhivya"}
c={"selvi","ravi","John"}
a.add("mouli")
print(a)
a.update(b)
print(a)
b.remove("Dhivya")
print(b)
x=a.union(b,c)
print(x)
a.pop()
print(a)
a.discard("Ruby")
print(a)
a.clear()
print(a)