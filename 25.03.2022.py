name=(input("Enter your name:"))
place=(input("where you want to go:"))
if(name=="jo"):
    if(place=="college"):
        print("Go straight you will reach that place")
    elif(place=="School"):
        print("Go straight turn right walk along the main road")
    else:
        print("place not found")

elif(name=="kavi"):
   
    if(place=="School"):
        print("Go straight turn left walk along the main road turn right")
    elif(place=="Temple"):
        print("Go straight turn right walk along the main road")
    else:
        print("place not found")

else:
    print("people not found")

