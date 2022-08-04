try:
    x=input("Enter the string")
    if (x=="a"or x=="e"or x=="i"or x=="o"or x=="i"or x=="o"or x=="u"):
        raise NameError
    else:
        print(x,"This string is not a vowel")
except:
    print(x,"This string is a vowel")
