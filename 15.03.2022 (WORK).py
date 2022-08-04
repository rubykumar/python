amt=0
a=int(input("Enter number of electric unit"))
if a<=100:
    amt=0
if a>100 and a<=200:
    amt=(a-100)*5
if a>200:
    a=500+(a-200)*10
    print("Amount of Pay: " amt)

